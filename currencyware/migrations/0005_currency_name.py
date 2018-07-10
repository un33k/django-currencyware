# Generated by Django 2.0.6 on 2018-07-10 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencyware', '0004_currency_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='name',
            field=models.CharField(blank=True, help_text='Curreny name (english)', max_length=60, null=True, verbose_name='Name'),
        ),
    ]