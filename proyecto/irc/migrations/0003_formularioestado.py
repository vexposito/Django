# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-11 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irc', '0002_auto_20160711_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_BOT', models.IntegerField()),
            ],
        ),
    ]
