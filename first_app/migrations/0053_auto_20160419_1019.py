# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 04:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0052_auto_20160419_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='cname',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 4, 49, 59, 648512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 4, 49, 59, 647509, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 4, 49, 59, 649679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 4, 49, 59, 648008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 4, 49, 59, 650303, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 4, 49, 59, 648960, tzinfo=utc)),
        ),
    ]
