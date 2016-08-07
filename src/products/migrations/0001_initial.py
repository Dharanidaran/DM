# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProducts',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
                'verbose_name': 'My Products',
                'verbose_name_plural': 'My Products',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('media', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/Users/dharani/Documents/DM/static_cdn/protected'), blank=True, null=True, upload_to=products.models.download_media_location)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(default=9.99, null=True, max_digits=100, decimal_places=2)),
                ('sale_price', models.DecimalField(max_digits=100, blank=True, null=True, default=6.99, decimal_places=2)),
                ('managers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='managers_products')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], default='hd', max_length=20)),
                ('height', models.CharField(blank=True, null=True, max_length=20)),
                ('width', models.CharField(blank=True, null=True, max_length=20)),
                ('media', models.ImageField(blank=True, null=True, width_field='width', height_field='height', upload_to=products.models.thumbnail_location)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='myproducts',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.AddField(
            model_name='myproducts',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
