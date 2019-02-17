# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('pasword', models.CharField(max_length=30)),
                ('licenseNum', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleType', models.CharField(max_length=20)),
                ('status', models.BooleanField()),
                ('plateNum', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='rentals',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleetapp.User'),
        ),
    ]