# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-16 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dislikes',
            new_name='Dislike',
        ),
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
    ]
