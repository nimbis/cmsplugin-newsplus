# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_newsplus', '0002_auto_20150424_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication date'),
            preserve_default=True,
        ),
    ]
