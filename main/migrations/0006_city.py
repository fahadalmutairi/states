# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160314_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=5)),
                ('latitude', models.FloatField(max_length=9)),
                ('longitude', models.FloatField(max_length=9)),
                ('name', models.CharField(max_length=15, null=True)),
                ('county', models.CharField(max_length=15, null=True)),
                ('state', models.ForeignKey(to='main.State', null=True)),
            ],
        ),
    ]
