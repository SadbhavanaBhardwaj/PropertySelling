# Generated by Django 3.0 on 2020-02-16 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20200216_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='create_date',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime.now),
        ),
    ]
