# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-14 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triptricks', '0004_auto_20170911_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='number_days',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
    ]
