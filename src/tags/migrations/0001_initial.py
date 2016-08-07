# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
            ],
        ),
    ]
