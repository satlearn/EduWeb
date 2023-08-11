from django.db import models

# Create your models here.
class sign(models.Model):
    Username = models.CharField(max_length=25)    
    Email_id = models.EmailField(max_length=25)
    Phone_Number = models.DecimalField(decimal_places=0,max_digits=10)
    Password = models.CharField(max_length=25)
    Confirm_Password = models.CharField(max_length=25,default=None) 
    


