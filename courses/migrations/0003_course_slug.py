# Generated by Django 4.2.5 on 2023-09-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]