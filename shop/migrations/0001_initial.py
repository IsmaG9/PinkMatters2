# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'verbose_name': 'artist',
                'ordering': ('name',),
                'verbose_name_plural': 'artists',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'verbose_name': 'category',
                'ordering': ('name',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'verbose_name': 'label',
                'ordering': ('name',),
                'verbose_name_plural': 'labels',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d', blank=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(to='shop.Artist', related_name='products_artist')),
                ('category', models.ForeignKey(to='shop.Category', related_name='products')),
                ('label', models.ForeignKey(to='shop.Label', related_name='products_label')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
