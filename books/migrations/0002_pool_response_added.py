# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionPoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=50)),
                ('poll_date', models.DateField()),
            ],
            options={
                'db_table': 'opinionpoll',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=50)),
                ('poll', models.ForeignKey(verbose_name='the related poll', to='books.OpinionPoll')),
            ],
            options={
                'db_table': 'response',
            },
        ),
    ]
