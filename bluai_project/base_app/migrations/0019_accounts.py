# Generated by Django 4.2.4 on 2023-08-15 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0018_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True, help_text='Enter your Twitter profile link here.', null=True, verbose_name='Twitter Link')),
                ('facebook', models.URLField(blank=True, help_text='Enter your Twitter profile link here.', null=True, verbose_name='Facebook Link')),
                ('instagram', models.URLField(blank=True, help_text='Enter your Twitter profile link here.', null=True, verbose_name='Instagram Link')),
                ('linkedln', models.URLField(blank=True, help_text='Enter your Twitter profile link here.', null=True, verbose_name='Linkedln Link')),
            ],
        ),
    ]
