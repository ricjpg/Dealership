# Generated by Django 4.1.7 on 2023-03-29 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0007_remove_carmodel_brand_remove_carmodel_cartype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(null='NULL', on_delete=django.db.models.deletion.CASCADE, to='dealership.brand'),
            preserve_default='NULL',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='cartype',
            field=models.ForeignKey(null='NULL', on_delete=django.db.models.deletion.CASCADE, to='dealership.cartype'),
            preserve_default='NULL',
        ),
        migrations.AddField(
            model_name='carversion',
            name='id_brand',
            field=models.ForeignKey(null='NULL', on_delete=django.db.models.deletion.CASCADE, to='dealership.brand'),
            preserve_default='NULL',
        ),
        migrations.AddField(
            model_name='carversion',
            name='id_model',
            field=models.ForeignKey(null='NULL', on_delete=django.db.models.deletion.CASCADE, to='dealership.carmodel'),
            preserve_default='NULL',
        ),
    ]
