# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YAASapp', '0004_auction_current_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='bidder',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
