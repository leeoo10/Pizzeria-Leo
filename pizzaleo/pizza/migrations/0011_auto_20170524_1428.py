# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 13:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0010_auto_20170524_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
