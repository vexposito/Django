# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-11 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulariocrear',
            old_name='usuario',
            new_name='nombre',
        ),
    ]
