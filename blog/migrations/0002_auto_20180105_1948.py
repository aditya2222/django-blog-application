# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 14:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 5, 14, 18, 34, 560491, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 5, 14, 18, 34, 559488, tzinfo=utc)),
        ),
    ]
