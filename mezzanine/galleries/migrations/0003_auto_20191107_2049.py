# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-11-08 02:49
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='exif_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='exif_date',
            field=models.DateTimeField(null=True),
        ),
    ]