# Generated by Django 3.2.25 on 2024-03-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20240306_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite_car',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
