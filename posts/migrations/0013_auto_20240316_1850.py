# Generated by Django 3.2.25 on 2024-03-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20240316_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='production',
            field=models.IntegerField(default='2024'),
        ),
    ]
