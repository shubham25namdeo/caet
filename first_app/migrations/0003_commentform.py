# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20160331_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Chats',
            },
        ),
    ]
