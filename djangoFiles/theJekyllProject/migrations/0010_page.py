# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 13:27
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theJekyllProject', '0009_auto_20171106_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('permalink', models.CharField(max_length=2000)),
                ('content', ckeditor.fields.RichTextField()),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theJekyllProject.Repo')),
            ],
        ),
    ]
