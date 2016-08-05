# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
from django.conf import settings
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'MyProducts',
                'verbose_name': 'My Products',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('media', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/dharani/Documents/DM/static_cdn/protected'), upload_to=products.models.download_media_location, blank=True)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(null=True, max_digits=100, default=9.99, decimal_places=2)),
                ('sale_price', models.DecimalField(decimal_places=2, null=True, max_digits=100, default=6.99, blank=True)),
                ('managers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='managers_product', blank=True)),
                ('user', models.ForeignKey(default='1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type', models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], default='hd', max_length=20)),
                ('height', models.CharField(null=True, max_length=20, blank=True)),
                ('width', models.CharField(null=True, max_length=20, blank=True)),
                ('media', models.ImageField(null=True, width_field='width', height_field='height', upload_to=products.models.thumbnail_location, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='myproducts',
            name='products',
            field=models.ManyToManyField(to='products.Product', blank=True),
        ),
        migrations.AddField(
            model_name='myproducts',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
