# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180526_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]