from django.db import models
from django.contrib.auth.models import User 



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# De cette façon, vous pouvez accéder
#  aux informations de profil associées à un profil en utilisant la relation de clé étrangère Profile_information.user.

class Profile_information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    Birthday = models.DateField()
    Profession = models.CharField(max_length=150)
    Bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos')
    cover = models.ImageField(upload_to='photo_cover')
    location = models.TextField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    RELATION_CHOICES = [
        ('Celibataire', 'CELIBATAIRE'),
        ('En Couple', 'EN COUPLE'),
        ('Divorcé', 'DIVORCE'),
        ('Veuf', 'VEUF'),
        ('Veuve', 'VEUVE'),
    ]
    Rela_status = models.CharField(max_length=50, choices=RELATION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# fetch('https://restcountries.eu/v2/all')
#   .then(res => res.json())
#   .then(countries => {
#     let select = document.getElementById('country');

#     for (let i = 0; i < countries.length; i++) {
#       let option = document.createElement('option');
#       option.value = countries[i].name;
#       option.text = countries[i].name;
#       select.appendChild(option);
#     }
#   });
