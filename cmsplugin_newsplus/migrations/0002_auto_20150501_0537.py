# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cmsplugin_newsplus.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_newsplus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=cmsplugin_newsplus.models.get_default_pub_date, verbose_name='Publication date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(unique_for_date='pub_date', help_text='A slug is a short name which uniquely identifies the news item for this day', verbose_name='Slug'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(upload_to='news_images'),
            preserve_default=True,
        ),
    ]
