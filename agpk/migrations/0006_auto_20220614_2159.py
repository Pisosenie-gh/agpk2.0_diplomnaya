# Generated by Django 3.2.13 on 2022-06-14 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agpk', '0005_auto_20220614_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='check_out',
        ),
    ]