# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_pool_response_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='poll',
            field=models.ForeignKey(related_name='poll', verbose_name='the related poll', to='books.OpinionPoll'),
        ),
    ]
