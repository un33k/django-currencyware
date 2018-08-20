import os
import sys
import json
import codecs
import logging
import requests
from datetime import datetime

from django.conf import settings
from django.utils import timezone
from django.utils import translation
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from translate.storage import po
from toolware.utils.generic import get_days_ago

from ...currency import get_display
from ...models import Rate, Currency
from ... import defaults as defs

log = logging.getLogger(__name__)


class Command(BaseCommand):
    # Experimental 
    help = "Fetches live rates from Google translation api"
    path = os.path.abspath(os.path.join(os.path.realpath(__file__), '../../../', 'locale'))
    from_locale = 'en'
    GOOGLE_TRANSLATE_URL = defs.GOOGLE_TRANSLATE_URL
    GOOGLE_API_KEY = defs.GOOGLE_API_KEY
    
    def add_arguments(self, parser):
        parser.add_argument(
            '-l',
            '--locale',
            dest='locale',
            help='Translate locale of for language.'
        )

    def handle(self, *args, **options):
        self.verbosity = options['verbosity']
        print(options)
        locale = options.get('locale')
        if not locale:
            self.print_help("", subcommand='currency')
            return

        locales = locale.split(' ')
        self.process(locales)


    def process(self, locales):
        if self.verbosity > 2:
            self.stdout.write('Preparing to fetch translations for locale {} ...'.format(locale))

        from_locale = os.path.join(self.path, self.from_locale, 'LC_MESSAGES', 'django.po')
        with codecs.open(from_locale, encoding='utf-8') as from_fp:
            from_fp.read()
            # from_blocks = po.pofile()
            # for block in from_blocks.units:
            #     print(block)
        
            return
            # for locale in locales:
            #     to_locale = os.path.join(self.path, locale, 'LC_MESSAGES', 'django.po')
            #         with codecs.open(to_locale, 'a+', encoding='utf-8') as to_fp:

            #     self.xlate(to_fp, locale)

    def xlate(self, from_fp, locale):
        to_locale = os.path.join(self.path, locale, 'LC_MESSAGES', 'django.po')
        with codecs.open(to_locale, 'a+', encoding='utf-8') as fp:
            return 

        if os.path.isfile(next):
            
            locale = locale.replace('_', '-').lower()

        resp = requests.get(
            self.GOOGLE_TRANSLATE_URL,
            params={
                'key': self.GOOGLE_API_KEY,
                'q': query,
                'source': 'en',
                'target': locale
            }
        )

        if resp.status_code != requests.codes.ok:
            self.stdout.write('Failed to fetch rates ...')
            self.stdout.write(resp.text)
            return
