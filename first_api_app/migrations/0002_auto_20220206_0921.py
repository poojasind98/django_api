# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2022-02-06 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexmodel',
            name='id',
            field=models.CharField(blank=True, max_length=11, primary_key=True, serialize=False),
        ),
    ]