# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetapp', '0002_auto_20160902_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentals',
            name='dateRent',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rentals',
            name='returnDate',
            field=models.DateTimeField(),
        ),
    ]