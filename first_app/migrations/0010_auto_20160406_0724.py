# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 01:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_commentform_dates'),
    ]

    operations = [
        migrations.CreateModel(
            name='loggedin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_loggedin', models.BooleanField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.UserProfile')),
            ],
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 1, 54, 24, 964964, tzinfo=utc)),
        ),
    ]