# Generated by Django 4.1.7 on 2023-03-26 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0003_rename_observation_brand_brand_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='cartype',
        ),
    ]
