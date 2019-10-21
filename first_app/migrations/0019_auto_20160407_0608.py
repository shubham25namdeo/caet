# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 00:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0018_auto_20160406_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 0, 38, 41, 529102, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 0, 38, 41, 528639, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 7)),
        ),
    ]