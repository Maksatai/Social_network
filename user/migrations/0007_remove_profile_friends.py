# Generated by Django 3.2.6 on 2021-10-05 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
    ]