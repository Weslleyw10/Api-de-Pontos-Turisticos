# Generated by Django 3.1.7 on 2021-04-08 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviews_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]