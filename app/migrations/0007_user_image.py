# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180521_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='static/no-img.jpg', upload_to='static/'),
        ),
    ]
