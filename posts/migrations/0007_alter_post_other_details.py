# Generated by Django 3.2.25 on 2024-03-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='other_details',
            field=models.CharField(max_length=260),
        ),
    ]