from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Data


# Create your views here.

def base(req):
    return render(req,'base.html')
def landing(req):
    return render(req,'landing.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Data

def Register(req):
    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')

        
        if p != cp:
            messages.error(req, 'Password does not match')
            return redirect('Register')

        
        if Data.objects.filter(Email=e).exists():
            messages.error(req, 'Email already exists')
            return redirect('Register')

        Data.objects.create(
            Name=n,
            Email=e,
            Contact=c,
            Password=p
        )

        messages.success(req, 'Registration successful')
        return redirect('Login')

    return render(req, 'Register.html')

def login(req):
    if 'admin_e' in req.session or 'user_id' in req.session:
        if 'admin_e' in req.session:
            data = {
                'email': req.session['admin_e'],
                'name': req.session['admin_n']
            }
            return render(req, 'adminpanel.html', {'data': data})
        elif 'user_id' in req.session:
            u_id=req.session.get('user_id')
            userdata=Data.objects.get(id=u_id)
            data={
                'name':userdata.name,
                'email':userdata.email,
                'contact':userdata.contact,
                'department':userdata.department
            }
            
            return render(req,'userpanel.html',{'data':data})
    else:
           
        if req.method == 'POST':
            e = req.POST.get('email')
            p = req.POST.get('password')

            print(e,p)
            print(type(p))
            if e == 'admin@gmail.com' and p == 'admin123':
                req.session['admin_e'] = e
                req.session['admin_n'] = 'Admin'
                return redirect('adminpanel')

            
            # user = Employee.objects.filter(email=e)
            print(user)
            if user:
                # userdata=Employee.objects.get(email=e)
                print(type(userdata.contact),type(p),p,userdata.contact)
                if p == userdata.contact:
                    req.session['user_id'] = userdata.id
                    print('userpanel')
                    return redirect('userpanel')
                else:
                    req.session['y'] = 'Email and password do not match'
            else:
                req.session['y'] = 'User does not exist'

            return redirect('login')

        y = req.session.pop('y', '')
        return render(req, 'login.html', {'y': y})        



def adminpanel(req):
    return render(req,'adminpanel.html')