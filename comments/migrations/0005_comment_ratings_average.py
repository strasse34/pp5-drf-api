# Generated by Django 3.2.25 on 2024-03-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ratings_average',
            field=models.FloatField(default=0),
        ),
    ]
