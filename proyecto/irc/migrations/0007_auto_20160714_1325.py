# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-14 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irc', '0006_bot_info_eventos_mensajes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot_info',
            name='SERVIDOR',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bot_info',
            name='INICIO',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bot_info',
            name='ULTIMA',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='FECHA',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='FECHA',
            field=models.IntegerField(),
        ),
    ]
