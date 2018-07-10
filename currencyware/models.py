from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from toolware.utils.query import CaseInsensitiveManager
from .currency import get_all_currencies_prioritized


class Currency(models.Model):
    code = models.CharField(
        # Note: admin:skip
        _('CURRENCY.CODOE'),
        max_length=3,
        primary_key=True,
        null=False,
        blank=False,
        # Note: admin:skip
        help_text=_('CURRENCY.CODE.DESC')
    )

    number = models.CharField(
        # Note: admin:skip
        _('CURRENCY.NUMBER'),
        max_length=3,
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('CURRENCY.NUMBER.DESC'),
    )

    unit = models.IntegerField(
        # Note: admin:skip
        _('CURRENCY.UNITS'),
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('CURRENCY.UNITS.DESC')
    )

    country = models.CharField(
        # Note: admin:skip
        _('CURRENCY.COUNTRY'),
        max_length=255,
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('CURRENCY.COUNTRY.DESC'),
    ) 

    # ########## Add new fields above this line #############
    objects = CaseInsensitiveManager()

    CASE_INSENSITIVE_FIELDS = ['code', ]

    @property
    def name(self):
        key = 'ISO_4217.' + self.code.upper()
        name = _(key)
        if name == key:
            return self.code
        return name

    def __str__(self):
        return self.name

    class Meta:
        # Note: admin:skip
        verbose_name=_('CURRENCY.LABEL.SINGULAR')
        # Note: admin:skip
        verbose_name_plural=_('CURRENCY.LABEL.PLURAL')


class Rate(models.Model):
    code = models.CharField(
        # Note: admin:skip
        _('RATE.CURRENCY.CODE'),
        max_length=3,
        choices=get_all_currencies_prioritized(),
        # Note: admin:skip
        help_text=_('RATE.CURRENCY.CODE.DESC'),
    )

    rate = models.FloatField(
        # Note: admin:skip
        _('RATE.CURRENCY'),
        null=False,
        blank=False,
        default=0.0,
        # Note: admin:skip
        help_text=_('RATE.CURRENCY.DESC'),
    )

    date = models.DateTimeField(
        # Note: admin:skip
        _('RATE.DATE'),
        null=False,
        blank=False,
        # Note: admin:skip
        help_text=_('RATE.DATE.DESC'),
    )

    # ########## Add new fields above this line #############
    objects = CaseInsensitiveManager()

    CASE_INSENSITIVE_FIELDS = ['code', ]

    class Meta:
        # Note: admin:skip
        verbose_name=_('RATE.LABEL.SINGULAR')
        # Note: admin:skip
        verbose_name_plural=_('RATE.LABEL.PLURAL')
