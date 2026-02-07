from django.db import models

# Create your models here.

class Data(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Contact=models.CharField(max_length=15)
    Password=models.CharField(max_length=20)
    
    
