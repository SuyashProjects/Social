# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-19 00:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180519_0551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mail',
            new_name='email',
        ),
    ]
