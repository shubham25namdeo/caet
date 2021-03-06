# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 00:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0051_auto_20160419_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
                ('log_user', models.CharField(default='ADMIN', max_length=30)),
                ('dates', models.DateTimeField(default=datetime.datetime(2016, 4, 19, 0, 38, 29, 962406, tzinfo=utc))),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 0, 38, 29, 960693, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 0, 38, 29, 959730, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 0, 38, 29, 961833, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 0, 38, 29, 960211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 0, 38, 29, 961130, tzinfo=utc)),
        ),
    ]
