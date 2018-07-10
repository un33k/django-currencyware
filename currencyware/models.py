from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from toolware.utils.query import CaseInsensitiveManager, CaseInsensitiveUniqueManager
from .currency import get_all_currencies_prioritized, get_display


class Currency(models.Model):
    code = models.CharField(
        # Note: admin:skip
        _('Code'),
        max_length=3,
        primary_key=True,
        null=False,
        blank=False,
        # Note: admin:skip
        help_text=_('Currency code')
    )

    number = models.CharField(
        # Note: admin:skip
        _('Number'),
        max_length=3,
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('Numeric code'),
    )

    unit = models.IntegerField(
        # Note: admin:skip
        _('Unit'),
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('Currency unit')
    )

    symbol = models.CharField(
        # Note: admin:skip
        _('Symbol'),
        max_length=10,
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('Currency symbol'),
    )

    country = models.CharField(
        # Note: admin:skip
        _('Country'),
        max_length=255,
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('Primary currency in these countries'),
    ) 

    # ########## Add new fields above this line #############
    objects = CaseInsensitiveUniqueManager()

    CASE_INSENSITIVE_FIELDS = ['code', ]

    @property
    def name(self):
        name = get_display(self.code)
        if self.code in name:
            name = self.code
        return name

    def __str__(self):
        return self.name

    class Meta:
        # Note: admin:skip
        verbose_name=_('Currency')
        # Note: admin:skip
        verbose_name_plural=_('Currencies')


class Rate(models.Model):
    code = models.CharField(
        # Note: admin:skip
        _('Code'),
        max_length=3,
        choices=get_all_currencies_prioritized(),
        # Note: admin:skip
        help_text=_('Currency code'),
    )

    rate = models.FloatField(
        # Note: admin:skip
        _('Rate'),
        null=False,
        blank=False,
        default=0.0,
        # Note: admin:skip
        help_text=_('Currency forex rate'),
    )

    date = models.DateTimeField(
        # Note: admin:skip
        _('Date'),
        null=False,
        blank=False,
        # Note: admin:skip
        help_text=_("Rate's date"),
    )

    # ########## Add new fields above this line #############
    objects = CaseInsensitiveManager()

    CASE_INSENSITIVE_FIELDS = ['code', ]

    class Meta:
        # Note: admin:skip
        verbose_name=_('Rate')
        # Note: admin:skip
        verbose_name_plural=_('Rates')
