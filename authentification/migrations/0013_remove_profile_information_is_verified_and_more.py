# Generated by Django 4.1.6 on 2023-02-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0012_profile_information_is_verified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_information',
            name='is_verified',
        ),
        migrations.AlterField(
            model_name='profile_information',
            name='Birthday',
            field=models.DateField(),
        ),
    ]
