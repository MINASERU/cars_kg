# Generated by Django 4.2.1 on 2023-05-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_category_photo_alter_vehicle_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0.0, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='slug',
            field=models.SlugField(default=0.0, max_length=100, unique=True),
        ),
    ]
