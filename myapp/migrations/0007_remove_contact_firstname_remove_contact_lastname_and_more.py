# Generated by Django 4.1.5 on 2023-01-31 22:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_contact_nom_remove_contact_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lastname',
        ),
        migrations.AddField(
            model_name='contact',
            name='nom',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]