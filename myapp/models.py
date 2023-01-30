from django.db import models

# Create your models here.
class Contact(models.Model) :
    nom = models.CharField(max_length=150 )
    email = models.EmailField()
    subject = models.CharField(max_length=500 )
    commentaire = models.TextField()
    
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now= True)
    date_update = models.DateTimeField(auto_now= True)
    
    def str(self) :
        return self.nom