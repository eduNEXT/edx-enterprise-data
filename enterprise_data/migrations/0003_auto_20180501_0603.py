# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-01 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0002_auto_20180430_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterpriseenrollment',
            old_name='enterprise_sso_site_id',
            new_name='enterprise_site_id',
        ),
    ]