# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0002_auto_20161118_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
