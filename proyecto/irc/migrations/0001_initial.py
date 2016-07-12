# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-30 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioCrear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servidor', models.CharField(max_length=100)),
                ('puerto', models.IntegerField()),
                ('canal', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('patron', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FormularioParar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_BOT', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FormularioRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('codigo_postal', models.IntegerField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]