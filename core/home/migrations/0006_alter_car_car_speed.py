# Generated by Django 4.1.7 on 2023-08-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_car_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_speed',
            field=models.IntegerField(default=50),
        ),
    ]
