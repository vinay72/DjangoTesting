# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-05 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contributor',
            options={'ordering': ['login']},
        ),
    ]