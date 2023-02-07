from django.db import models
from django.contrib.auth.models import User 



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to='profile_photos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username






