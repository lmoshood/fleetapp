# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentals',
            name='dateRent',
            field=models.DateTimeField(default='2016-01-01 00:00:00'),
        ),
        migrations.AddField(
            model_name='rentals',
            name='returnDate',
            field=models.DateTimeField(default='2016-01-01 00:00:00'),
        ),
        migrations.AlterField(
            model_name='user',
            name='licenseNum',
            field=models.CharField(max_length=30),
        ),
    ]