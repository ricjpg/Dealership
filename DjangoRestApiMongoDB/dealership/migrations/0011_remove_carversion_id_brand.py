# Generated by Django 4.1.7 on 2023-03-30 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0010_alter_brand_brand_name_alter_carcolor_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carversion',
            name='id_brand',
        ),
    ]
