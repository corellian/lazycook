# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('rating', models.IntegerField()),
                ('prep_time', models.TimeField(verbose_name=b'preparation time')),
                ('cook_time', models.TimeField(verbose_name=b'cooking time')),
                ('diners', models.IntegerField()),
                ('difficulty', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
