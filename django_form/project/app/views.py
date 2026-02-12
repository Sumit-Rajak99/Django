from django.shortcuts import render,redirect
from .forms import Studentform

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def Regisetion(req):
    if req.method=='POST':
        form=Studentform(req.POST)
        
        print(form)
        print(form.cleaned_data)
        # print("hello django")
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('login')
    data = Studentform()
    return render(req,'Regisetion.html',{'data':data})
