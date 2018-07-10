import sys
import json
import codecs
import logging
import requests
from datetime import datetime

from django.utils import timezone
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from toolware.utils.generic import get_days_ago

from ...models import Rate, Currency
from ... import defaults as defs

log = logging.getLogger(__name__)


class Command(BaseCommand):
    # Translators: admin
    help = "Fetches live rates from open exchange rates api"

    OXR_URL = defs.OPEN_EXCHANGE_RATES_URL
    OXR_KEY = defs.OPEN_EXCHANGE_RATES_API_KEY

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--flush',
            action='store_true',
            dest='flush',
            default=False,
            help='Remove all rates from db'
        )

        parser.add_argument(
            '-p',
            '--purge',
            action='store',
            dest='days',
            type=int,
            default=-1,
            help='Remove rates older than x days'
        )

        parser.add_argument(
            '-l',
            '--load',
            action='store_true',
            dest='load',
            default=False,
            help='Fetch and load all rates to db'
        )

    def handle(self, *args, **options):
        self.verbosity = options['verbosity']
        self.days = options['days']
        self.flush = options['flush']
        self.load = options['load']

        if self.flush:
            self.stdout.write('You are about to delete all rates from db')
            confirm = input('Are you sure? [yes/no]: ')
            if confirm == 'yes':
                Rate.objects.all().delete()
                self.stdout.write('Flushed rates from db.')

        if self.verbosity > 2:
            self.stdout.write('Preparing to fetch rates ...')

        if self.days >= 0:
            days_ago = get_days_ago(self.days)
            Rate.objects.filter(date__lte=days_ago).delete()
            self.stdout.write('Purged rates older than ({}) ago from db.'.format(self.days))

        if not self.load:
            return

        resp = requests.get(self.OXR_URL, params={'app_id': self.OXR_KEY})
        if resp.status_code != requests.codes.ok:
            self.stdout.write('Failed to fetch rates ...')
            self.stdout.write(resp.text)
            return

        self.data = resp.json()

        new_count, update_count = 0, 0
        updated = datetime.fromtimestamp(self.data['timestamp'], tz=timezone.utc)
        for code, rate in self.data['rates'].items():
            created = False
            defaults = {
                'code': code,
                'rate': rate,
                'date': updated
            }
            instance, created = Rate.objects.get_or_create_unique(defaults, ['code'])
            if created:
                new_count += 1
            else:
                update_count += 1
            
            if not instance and self.verbosity >=3:
                sys.stdout.write('Failed to create rate for ({code})\n'.format(code=code))

        self.stdout.write('Created {count} currenies'.format(count=new_count))
        self.stdout.write('Updated {count} currenies'.format(count=update_count))
