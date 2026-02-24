from django.db import models

# Create your models here.
class Data(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Course=models.CharField(max_length=20)
    Contact=models.IntegerField()
    Email=models.EmailField()
    City=models.CharField(max_length=20)
