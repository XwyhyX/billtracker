# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_auto_20160605_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='dueDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
