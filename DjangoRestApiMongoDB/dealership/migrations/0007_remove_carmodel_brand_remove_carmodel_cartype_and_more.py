# Generated by Django 4.1.7 on 2023-03-29 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0006_carmodel_cartype_alter_brand_brand_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='cartype',
        ),
        migrations.RemoveField(
            model_name='carversion',
            name='id_brand',
        ),
        migrations.RemoveField(
            model_name='carversion',
            name='id_model',
        ),
    ]
