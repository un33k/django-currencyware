from django.contrib import admin

from .models import Currency, Rate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'number', 'unit', )
    search_fields = ('code', )
    ordering = ['code']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('code', 'rate', 'date', )
    search_fields = ('code', )
    ordering = ['code']
