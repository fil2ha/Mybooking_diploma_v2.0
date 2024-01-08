# Generated by Django 5.0 on 2023-12-20 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата заезда'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата выезда'),
        ),
    ]
