# Generated by Django 3.2.25 on 2024-03-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_remove_comment_ratings_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ratings_average',
            field=models.FloatField(default=0),
        ),
    ]
