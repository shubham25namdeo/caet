# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20160401_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentform',
            name='logged_inuser',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
