# Generated by Django 4.1.5 on 2023-02-05 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
                ('drapeau', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_photos'),
            preserve_default=False,
        ),
    ]