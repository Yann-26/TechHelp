from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class ProfileInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = CountryField()
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField()
    profession = models.CharField(max_length=150)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos')
    cover = models.ImageField(upload_to='photo_cover')
    location = models.TextField(blank=True)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    RELATION_CHOICES = (
        ('Celibataire', 'CÉLIBATAIRE'),
        ('En Couple', 'EN COUPLE'),
        ('Divorcé', 'DIVORCE'),
        ('Veuf', 'VEUF'),
        ('Veuve', 'VEUVE'),
    )
    rela_status = models.CharField(max_length=50, choices=RELATION_CHOICES)
    
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
