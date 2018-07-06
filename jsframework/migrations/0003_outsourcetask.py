# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0002_auto_20150527_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutSourceTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', jsonfield.fields.JSONField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
