from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.email


class Banner(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300)
    bouton1 = models.CharField(max_length=10)
    bouton2 = models.CharField(max_length=10)

    #STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) :
        return self.title


class Navbar(models.Model):
    logo = models.ImageField()
    home = models.CharField(max_length=50)
    slogan = models.CharField(max_length=50)
    dropdown = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    blog_grid = models.CharField(max_length=50)
    blog_detail = models.CharField(max_length=50)
    features = models.CharField(max_length=50)
    quote = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    testimonial = models.CharField(max_length=50)

    #STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) :
        return self.home

class Topbar(models.Model):
    paqs = models.CharField(max_length=50)
    support = models.CharField(max_length=50)
    privacy = models.CharField(max_length=50)
    policy = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    my_mail = models.EmailField()
    number = models.CharField(max_length=20)

    #STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) :
        return self.home


class contactUs(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    mapUrl = models.TextField()

    #STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) :
        return self.title
    
