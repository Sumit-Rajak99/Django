from django.shortcuts import render

# Create your views here.

def index(req):
    d={'n':'sumit',
       'a':'Fullstack',
       'c':'BHOPAL',
       'p':"this is django class"}
    return render(req,'index.html',{'data':d})
