# Generated by Django 4.1.6 on 2023-05-10 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_reponse_commentaire_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse_commentaire',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reponses', to='myapp.comment'),
        ),
    ]
