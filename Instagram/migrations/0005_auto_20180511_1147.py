# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0004_image_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_path',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]