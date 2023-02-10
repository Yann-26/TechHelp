# Generated by Django 4.1.6 on 2023-02-10 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentification', '0010_profile_address_profile_bio_profile_birthday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Birthday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Profession',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Rela_status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_photo',
        ),
        migrations.CreateModel(
            name='Profile_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('Birthday', models.DateField()),
                ('Profession', models.CharField(max_length=150)),
                ('Bio', models.TextField()),
                ('profile_photo', models.ImageField(upload_to='profile_photos')),
                ('cover', models.ImageField(upload_to='photo_cover')),
                ('location', models.TextField()),
                ('Rela_status', models.CharField(choices=[('Celibataire', 'CELIBATAIRE'), ('En Couple', 'EN COUPLE'), ('Divorcé', 'DIVORCE'), ('Veuf', 'VEUF'), ('Veuve', 'VEUVE')], max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Address', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
