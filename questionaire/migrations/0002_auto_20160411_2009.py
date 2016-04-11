# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 20:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questionaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 8, 36, 809628, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 8, 47, 909629, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 8, 55, 116328, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerset',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 9, 2, 893512, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 9, 10, 313477, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 9, 15, 540690, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 9, 21, 311937, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionaire',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 20, 9, 29, 998344, tzinfo=utc)),
            preserve_default=False,
        ),
    ]