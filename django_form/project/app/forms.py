from .models import Student
from django import forms
# class Studentform(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     age=forms.IntegerField()
#     city=forms.CharField()

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    