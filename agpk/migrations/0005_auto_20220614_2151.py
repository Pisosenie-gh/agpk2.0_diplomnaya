# Generated by Django 3.2.13 on 2022-06-14 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agpk', '0004_auto_20220613_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='price',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='size',
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
