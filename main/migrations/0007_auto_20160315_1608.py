# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='county',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='zip_code',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
