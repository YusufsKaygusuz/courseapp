# Generated by Django 4.2.5 on 2023-09-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_category_slug_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
