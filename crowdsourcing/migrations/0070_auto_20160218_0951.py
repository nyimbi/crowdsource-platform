# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0069_auto_20160218_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='job_tag',
            new_name='job_title',
        ),
    ]
