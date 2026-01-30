from .models import Employee
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render,redirect
import random

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def forget(req):
    return render(req,'forget.html')

def otp(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        otp_code=random.randint(111111,999999)
        req.session['email']=email
        req.session['otp']=otp_code
        send_mail(
            subject="Forget password",
            message=f'User Email OTP: {otp_code}',
            from_email="sumitrajaksumitrajak793@gmail.com",  
            recipient_list=[email],
            fail_silently=False,
        )
        return render(req, 'otp.html')

    return render(req, 'otp.html')

def newpassword(req):
    if req.method == 'POST':
        user_otp = req.POST.get('otp')
        store_otp = req.session.get('otp')

        if str(user_otp) == str(store_otp):
            email = req.session.get('email')
            return render(req, 'newpassword.html',{'email':email})
        
        else:
            
            return render(req, 'otp.html', {'error': 'Invalid OTP'})
    email = req.session.get('email')
    return render(req,'newpassword.html',{'email':email})

def newpass(req):
    if req.method=='POST':
        e = req.POST.get('email')
        p = req.POST.get('npass')
        cp = req.POST.get('cnpass')
        if p == cp:
            userdata = Employee.objects.get(email=e)
            userdata.password=p
            userdata.save()
            messages.info(req,'Password reset successfully')
            return redirect('landing')
        else:
            messages.info(req,'Password and conform password not matched')
            return redirect('newpassword')
        