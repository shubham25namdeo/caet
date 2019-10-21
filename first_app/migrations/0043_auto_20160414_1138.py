# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 06:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0042_auto_20160414_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 8, 9, 960610, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 8, 9, 959110, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 8, 9, 963008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='log_user',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='note',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 8, 9, 959990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 8, 9, 961323, tzinfo=utc)),
        ),
    ]