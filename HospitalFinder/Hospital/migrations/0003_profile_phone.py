# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='8790089990', max_length=20),
            preserve_default=False,
        ),
    ]
