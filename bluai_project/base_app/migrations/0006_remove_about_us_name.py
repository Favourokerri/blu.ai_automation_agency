# Generated by Django 4.2.4 on 2023-08-13 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_about_us_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_us',
            name='name',
        ),
    ]
