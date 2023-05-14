from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.mail import send_mail

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    commentaire = models.TextField()

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

#######################################################################################################################################################################
# DEBUT SYSTEME DE COMMENTAIRE 

class Comment(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    commenter = models.TextField()


    #STANDARS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)  
    
    def __str__(self):
        return self.email
    
class Reponse_Commentaire(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    reponse_comment = models.TextField()
    parent_comment = models.ForeignKey(on_delete=models.CASCADE, to=Comment, related_name='reponses' )

    #STANDARS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.reponse_comment

class Policy(models.Model):
    policy = models.TextField()
    privacy = models.TextField()
      # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.policy


# FIN SYSTEME DE COMMENTAIRE 
#######################################################################################################################################################################

class TeamMembers(models.Model):
    fullname =models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    photo = models.ImageField()

    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.fullname





# ################### newsletter
### CREATION D4ABONNEES 
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"

####CREATION DE NEWSLETTERS
class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='uploaded_newsletters/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        for sub in subscribers:
            email_subject = self.subject
            email_body = contents + (
                '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                    request.build_absolute_uri('/delete/'),
                    sub.email,
                    sub.conf_num)
            send_mail(email_subject, email_body, settings.FROM_EMAIL, [sub.email], html_message=email_body)

# //////////////////////DASHBOARD

class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)


    
