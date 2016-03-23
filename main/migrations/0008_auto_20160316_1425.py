# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160315_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.FloatField(max_length=9, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.FloatField(max_length=9, null=True, blank=True),
        ),
    ]
