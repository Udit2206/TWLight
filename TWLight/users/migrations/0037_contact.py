# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 09:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0036_auto_20190107_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text="Author's email address", max_length=50)),
                ('message', models.TextField(blank=True, help_text='Message from the author.', max_length=1000)),
                ('author', models.ForeignKey(blank=True, help_text='User who authored this query.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
