# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YAASapp', '0003_auto_20161107_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='current_bid',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
