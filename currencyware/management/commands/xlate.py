import re
import os
import sys
import json
import codecs
import logging
import requests
from datetime import datetime
import polib

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

        parser.add_argument(
            '-o',
            '--overwrite',
            dest='overwrite',
            default=False,
            help='Overwrite translated items.'
        )

    def handle(self, *args, **options):
        self.verbosity = options['verbosity']
        locale = options.get('locale')
        self.overwrite = options.get('overwrite')
        if not locale:
            self.print_help("", subcommand='currency')
            return

        locales = locale.split(' ')
        if locales:
            if self.verbosity > 2:
                self.stdout.write('Preparing to fetch translations for locale {} ...'.format(locale))

            source_path = os.path.join(self.path, self.from_locale, 'LC_MESSAGES', 'django.po')
            source_po = polib.pofile(source_path)
            source_pairs = self.get_source_msg_pairs(source_po)

            for target in locales:
                self.process_target(source_pairs, target)

        
    def process_target(self, source_pairs, target_locale):
        target_path = os.path.join(self.path, target_locale, 'LC_MESSAGES', 'django.po')
        target_po = polib.pofile(target_path)
        target_pairs = self.get_source_msg_pairs(target_po)

        self.stdout.write('Processing {} ...'.format(target_locale))
        for index, pair in enumerate(source_pairs):
            text = pair[1]
            success, value = self.xlate(text, target_locale)
            if not success:
                break
            if self.verbosity > 1:
                print(text, value, target)
            target_po[index].msgstr = value
            target_po.save()

            #  print(resp)
            # from_blocks = po.pofile()
            # for block in from_blocks.units:
            #     print(block)
        
        return
            # for locale in locales:
            #     to_locale = os.path.join(self.path, locale, 'LC_MESSAGES', 'django.po')
            #         with codecs.open(to_locale, 'a+', encoding='utf-8') as to_fp:

            #     self.xlate(to_fp, locale)

    # def xlate(self, from_fp, locale):
    #     to_locale = os.path.join(self.path, locale, 'LC_MESSAGES', 'django.po')
    #     with codecs.open(to_locale, 'a+', encoding='utf-8') as fp:
    #         return 

    #     if os.path.isfile(next):
            
    #         locale = locale.replace('_', '-').lower()

    #     resp = requests.get(
    #         self.GOOGLE_TRANSLATE_URL,
    #         params={
    #             'key': self.GOOGLE_API_KEY,
    #             'q': query,
    #             'source': 'en',
    #             'target': locale
    #         }
    #     )

    #     if resp.status_code != requests.codes.ok:
    #         self.stdout.write('Failed to fetch rates ...')
    #         self.stdout.write(resp.text)
    #         return

    def get_source_msg_pairs(self, po):
        """
        Returns translated msg (id:str) from a po file
        """
        msg_pairs = []
        for index, item in enumerate(po):
            msg_pairs.append((item.msgid, self.pre_translate_cleanup(item.msgstr)))
        return msg_pairs

    def should_translate(self, item):
        if item.obsolete:
            return False
        if item.translated() and self.overwrite:
            return True
    
    def pre_translate_cleanup(self, msgid):
        """
        Best attempt to ensure google doesn't translate the following
        %(name)s -> __name__
        %s       -> __item__
        %d       -> __number__
        """
        return re.sub(
            r'%(?:\((\w+)\))?([sd])',
            lambda match: r'__{0}__'.format(
                match.group(1).lower() if match.group(1) else 'number' if match.group(2) == 'd' else 'item'),
            msgid)
    

    def xlate(self, text, target, source='en'):
        resp = requests.get(
            self.GOOGLE_TRANSLATE_URL,
            params={
                'key': self.GOOGLE_API_KEY,
                'q': text,
                'source': source,
                'target': target
            }
        )

        if resp.status_code != requests.codes.ok:
            self.stdout.write('Failed to fetch rates ...')
            self.stdout.write(resp.text)
            return (False, None)

        return (True, resp.json()['data']['translations'][0]['translatedText'])
