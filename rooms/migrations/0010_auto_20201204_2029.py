# Generated by Django 3.1.3 on 2020-12-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20201204_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Цена номера'),
        ),
    ]
