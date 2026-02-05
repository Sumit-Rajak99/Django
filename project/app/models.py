from django.db import models

# Create your models here.

class Student(models.Model):
   email=models.CharField(max_length=10)
   password = models.CharField(max_length=20)
   
class Department(models.Model):
   d_name=models.CharField(max_length=20)
   d_head=models.CharField(max_length=20)
   

class Employee(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.CharField() 
    contact = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=20)
  

class password(models.Model):
   name=models.CharField(max_length=20)
   email=models.EmailField(unique=True)
   password=models.CharField(max_length=20)   
   
class Query(models.Model):
   Name=models.CharField(max_length=20)
   Email=models.EmailField()
   Query=models.TextField()
   Department=models.CharField(max_length=50)
   Status=models.CharField(max_length=50,default='pending')
   Admin_replay=models.CharField( max_length=250)
      
   
      
   
