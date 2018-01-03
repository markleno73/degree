# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapps', '0002_auto_20171012_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='address',
        ),
        migrations.AddField(
            model_name='places',
            name='address_line1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='places',
            name='address_line2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='places',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='places',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='places',
            name='zip',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Addresses',
        ),
    ]
