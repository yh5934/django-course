# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-29 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='planner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_planner', to='LogReg.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='travelers',
            field=models.ManyToManyField(related_name='trip_travelers', to='LogReg.User'),
        ),
    ]
