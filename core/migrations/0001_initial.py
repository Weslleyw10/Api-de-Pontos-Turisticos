# Generated by Django 3.1.7 on 2021-04-07 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristSpots',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]