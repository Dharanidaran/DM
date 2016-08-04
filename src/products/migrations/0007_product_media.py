# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160804_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to=products.models.download_media_location),
        ),
    ]
