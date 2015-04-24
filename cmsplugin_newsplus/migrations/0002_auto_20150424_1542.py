# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_newsplus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 19, 42, 20, 509733, tzinfo=utc), verbose_name='Publication date'),
            preserve_default=True,
        ),
    ]
