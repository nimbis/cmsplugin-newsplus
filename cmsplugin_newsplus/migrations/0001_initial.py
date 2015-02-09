# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNewsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('limit', models.PositiveIntegerField(help_text='Limits the number of items that will be displayed', verbose_name='Number of news items to show')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(help_text='A slug is a short name which uniquely identifies the news item for this day', verbose_name='Slug', unique_for_date=b'pub_date')),
                ('excerpt', models.TextField(verbose_name='Excerpt', blank=True)),
                ('content', models.TextField(verbose_name='Content', blank=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Published')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 2, 9, 16, 52, 1, 765997, tzinfo=utc), verbose_name='Publication date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('link', models.URLField(help_text='This link will be used a absolute url for this item and replaces the view logic. <br />Note that by default this only applies for items with  an empty "content" field.', null=True, verbose_name='Link', blank=True)),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'news_images')),
                ('news', models.ForeignKey(related_name='images', to='cmsplugin_newsplus.News')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
