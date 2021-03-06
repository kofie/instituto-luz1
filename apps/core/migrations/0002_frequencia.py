# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.SmallIntegerField()),
                ('ano', models.SmallIntegerField()),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('beneficiado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Beneficiado')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
