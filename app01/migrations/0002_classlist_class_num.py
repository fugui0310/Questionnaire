# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlist',
            name='class_num',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
