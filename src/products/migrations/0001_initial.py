# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=100, null=True, default=9.99, decimal_places=2)),
                ('sale_price', models.DecimalField(blank=True, max_digits=100, null=True, default=6.99, decimal_places=2)),
            ],
        ),
    ]
