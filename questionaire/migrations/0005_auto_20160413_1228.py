# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionaire', '0004_auto_20160412_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='answers',
            field=models.CharField(default='[]', max_length=512),
        ),
    ]
