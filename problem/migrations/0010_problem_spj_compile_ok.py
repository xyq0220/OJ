# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0009_auto_20171011_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='spj_compile_ok',
            field=models.BooleanField(default=False),
        ),
    ]