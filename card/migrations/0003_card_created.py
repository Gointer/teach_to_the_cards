# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 15:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_card_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 24, 15, 35, 52, 406150, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
