# Generated by Django 3.1.3 on 2020-12-03 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomgallery',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.room', verbose_name='Галерея фото'),
        ),
    ]
