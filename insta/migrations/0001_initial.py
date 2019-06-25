# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 13:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.IntegerField(default=0)),
                ('comments', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('profile', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infor', models.IntegerField(default=0)),
                ('bio', models.CharField(max_length=70)),
                ('profile_picture', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['profile_picture'],
            },
        ),
    ]
