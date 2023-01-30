from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=17)
    genre = models.CharField(max_length=1)
    country = models.CharField(max_length=2)
    photo = models.ImageField(upload_to='profile_photos', blank=True)

    def __str__(self):
        return self.user.username


