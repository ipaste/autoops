# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 20:57
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarys',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='test', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='librarys',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='%Y%m%d70278'),
        ),
    ]
