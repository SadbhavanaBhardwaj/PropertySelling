# Generated by Django 3.0 on 2020-02-16 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200215_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='create_date',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2020, 2, 16, 21, 24, 57, 425549)),
        ),
    ]