# Generated by Django 3.0 on 2020-02-14 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20200215_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2020, 2, 15, 1, 20, 19, 828170)),
        ),
    ]