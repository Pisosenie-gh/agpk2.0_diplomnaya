# Generated by Django 3.2.13 on 2022-06-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agpk', '0007_remove_rooms_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='FIO',
            field=models.CharField(default='null', max_length=100, verbose_name='ФИО'),
        ),
    ]
