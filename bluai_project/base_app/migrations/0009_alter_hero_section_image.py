# Generated by Django 4.2.4 on 2023-08-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0008_alter_hero_section_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero_section',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='heros'),
        ),
    ]