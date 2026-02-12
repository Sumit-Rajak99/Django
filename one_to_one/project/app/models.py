from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar_no=models.IntegerField()
    create_date=models.DateField(auto_now_add=True)
    create_by=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.aadhar_no)
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    
    # aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)  # without related_name
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE, related_name='xyz')  # with related_name
        
