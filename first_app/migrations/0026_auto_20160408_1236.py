# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 07:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0025_auto_20160408_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 7, 6, 57, 337531, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 7, 6, 57, 336946, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 7, 6, 57, 337959, tzinfo=utc)),
        ),
    ]
