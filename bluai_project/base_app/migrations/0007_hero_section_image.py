# Generated by Django 4.2.4 on 2023-08-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0006_remove_about_us_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero_section',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hero-img'),
        ),
    ]
