# Generated by Django 4.2.4 on 2023-08-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0013_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default='blueai_worker', help_text='enter your name', max_length=100),
        ),
    ]