# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0018_remove_bills_billingmonth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bills',
            options={'ordering': ('-month', '-status'), 'verbose_name_plural': 'Bills'},
        ),
    ]
