# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Name',
            field=models.CharField(max_length=50, default='DEFAULT VALUE'),
        ),
        migrations.AddField(
            model_name='post',
            name='Roll_Number',
            field=models.CharField(max_length=9, default='DEFAULT VALUE'),
        ),
    ]
