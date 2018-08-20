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

from toolware.utils.generic import get_days_ago

from ...currency import get_display
from ...models import Rate, Currency
from ... import defaults as defs

log = logging.getLogger(__name__)


class Command(BaseCommand):
    # Translators: admin
    help = "Fetches live rates from Google translation api"
    path = os.path.abspath(os.path.join(os.path.realpath(__file__), '../../../', 'locale'))

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
        for locale in locales:
            self.translate(locale)


    def translate(self, locale):
        locale = locale.replace('_', '-')
        print('processing ({}) ...'.format(locale))       