# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_auto_20170524_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('pizza', models.ManyToManyField(related_name='pizza', to='pizza.Pizza')),
            ],
        ),
    ]
