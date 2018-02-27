# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 04:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0038_auto_20160414_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 4, 43, 30, 104626, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 4, 43, 30, 103668, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 4, 43, 30, 105805, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='joindate',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='note',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 4, 43, 30, 104146, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 4, 43, 30, 105112, tzinfo=utc)),
        ),
    ]
