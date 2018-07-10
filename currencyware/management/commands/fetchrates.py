import sys
import json
import codecs
import logging
import requests
import dateparser

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.utils.translation import ugettext as _
from django.utils import translation
from django.conf import settings
from datetime import datetime

from utilware.query import get_or_create_object
from ...models import Rate, Currency

from ... import defaults as defs

log = logging.getLogger(__name__)


class Command(BaseCommand):
    # Translators: admin
    help = _('COMMAND.RATES.LABEL')

    OXR_URL = defs.OPEN_EXCHANGE_RATE_URL
    OXR_KEY = defs.OPEN_EXCHANGE_RATE_API_KEY

    def add_arguments(self, parser):
        parser.add_argument(
            '-f', '--file', dest='file', default=None,
            # Translators: admin
            help=_('COMMAND.RATES.LOAD_JSON'),
        )

        parser.add_argument(
            '--flush',
            action='store_true', dest='flush', default=False,
            # Translators: admin
            help=_('COMMAND.RATES.FLUSH_HELP')
        )

        parser.add_argument(
            '--purge',
            action='store', dest='purge', default=None,
            # Translators: admin
            help=_('COMMAND.RATES.PURGE_HELP')
        )

    def handle(self, *args, **options):
        self.verbosity = options['verbosity']
        translation.activate(getattr(settings, 'LANGUAGE_CODE', 'en'))

        startdate = None

        if options['purge'] is not None:
            startdate = dateparser.parse(options['purge'])
            if startdate is None:
                # Translators: admin
                raise CommandError(_("ERROR.RATES.PARSE_DATE_FMT").format(date=options['purge']))

        if options['file']:
            self.get_rates_file(options['file'])
        else:
            self.get_rates_http()

        if options['flush']:
            self.flush()

        self.store_rates()

        if startdate is not None:
            ForexRate.objects.filter(date < startdate).delete()

    def flush(self):
        ForexRates.objects.all().delete()

    def get_rates_file(self, fname):
        try:
            self.data = json.load(fname)
        except:
            # Translators: admin
            raise CommandError(_("ERROR.FILE.PARSE_FMT").format(file=fname, error=sys.exc_info()[1]))

    def get_rates_http(self):
        try:
            r = requests.get(self.OER_URL, params={'app_id': settings.CONFIG_DATA['OER_API_KEY']})
        except:
            # Translators: admin
            raise CommandError(_('ERROR.CURRENCY.RETRIEVE_FMT').format(error=sys.exc_info()[1]))

        if r.status_code != requests.codes.ok:
            # Translators: admin
            raise CommandError(_('ERROR.CURRENCY.FAILED_FMT').format(error=r.text))

        try:
            self.data = r.json()
        except:
            # Translators: admin
            raise CommandError(_('ERROR.CURRENCY.PARSE_FMT').format(error=sys.exc_info()[1]))

    def store_rates(self):
        updated = datetime.fromtimestamp(self.data['timestamp'])

        for code, rate in self.data['rates'].items():
            # create or update related rates

            forex_obj, created = get_or_create_object(
                ForexRate,
                ['currency_code'],
                {
                    'currency_code': code,
                    'rate': rate, 'date': updated,
                }
            )

            if not forex_obj and self.verbosity >=3:
                sys.stdout.write('Failed to add/update ForexRate ({code})\n'.format(code=code))
