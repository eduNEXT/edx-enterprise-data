# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-01 09:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0003_auto_20180501_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterpriseenrollment',
            old_name='user_account_creation_date',
            new_name='user_account_creation_timestamp',
        ),
    ]