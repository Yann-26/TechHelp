# Generated by Django 4.1.6 on 2023-05-11 00:15

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0014_profileinformation_delete_profile_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinformation',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
