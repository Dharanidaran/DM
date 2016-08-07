# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
