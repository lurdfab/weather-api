# Generated by Django 4.2.6 on 2023-10-26 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='weather_descrition',
            new_name='weather_description',
        ),
    ]
