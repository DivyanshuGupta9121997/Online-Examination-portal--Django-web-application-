# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-10 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20161109_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='vericode',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
