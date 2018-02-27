# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 05:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0040_auto_20160414_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultant',
            old_name='logged_user',
            new_name='log_user',
        ),
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 45, 28, 416248, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 45, 28, 415097, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 45, 28, 417503, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 45, 28, 415727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 45, 28, 416734, tzinfo=utc)),
        ),
    ]
