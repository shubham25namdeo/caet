# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20160331_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=30)),
            ],
        ),
    ]
