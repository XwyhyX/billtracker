# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0006_bills_duedate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bills',
            options={'ordering': ('-id', '-status'), 'verbose_name_plural': 'Bills'},
        ),
        migrations.AddField(
            model_name='bills',
            name='billingMonth',
            field=models.DateField(default=django.utils.datetime_safe.date(2016,4,21)),
            preserve_default=False,
        ),
    ]
