# Generated by Django 4.1.6 on 2023-02-10 00:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0007_remove_profile_address_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_information',
            name='Rela_status',
            field=models.CharField(choices=[('Celibataire', 'CELIBATAIRE'), ('En Couple', 'EN COUPLE'), ('Divorcé', 'DIVORCE'), ('Veuf', 'VEUF'), ('Veuve', 'VEUVE')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile_information',
            name='location',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
