# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0010_bills_billingmonth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bills',
            old_name='billingMonth',
            new_name='billingMonth2',
        ),
    ]
