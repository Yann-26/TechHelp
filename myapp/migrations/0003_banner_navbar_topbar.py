# Generated by Django 4.1.5 on 2023-01-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=300)),
                ('bouton1', models.CharField(max_length=10)),
                ('bouton2', models.CharField(max_length=10)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('home', models.CharField(max_length=50)),
                ('slogan', models.CharField(max_length=50)),
                ('dropdown', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=50)),
                ('blog_grid', models.CharField(max_length=50)),
                ('blog_detail', models.CharField(max_length=50)),
                ('features', models.CharField(max_length=50)),
                ('quote', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('testimonial', models.CharField(max_length=50)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paqs', models.CharField(max_length=50)),
                ('support', models.CharField(max_length=50)),
                ('privacy', models.CharField(max_length=50)),
                ('policy', models.CharField(max_length=50)),
                ('career', models.CharField(max_length=50)),
                ('my_mail', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=20)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
