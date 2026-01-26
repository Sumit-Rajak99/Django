from django.shortcuts import render,redirect
from .models import Student


# Create your views here.

def base(req):
    return render(req,'base.html')
def landing(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')

def service(req):
    return render(req,'service.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')
             
def login(req):
    print(req.method)
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')

        print(e,p)
        if e == 'admin@gmail.com' and p == 'admin123':
            req.session['admin_e'] = e
            req.session['admin_n'] = 'Admin'
            return redirect('adminpanel')

        
        user = Student.objects.filter(email=e)

        if user:
            if p == user.password:
                req.session['user_id'] = user.id
                return redirect('adminpanel')
            else:
                req.session['y'] = 'Email and password do not match'
        else:
            req.session['y'] = 'User does not exist'

        return redirect('login')

    y = req.session.pop('y', '')
    return render(req, 'login.html', {'y': y})        
       
       

def adminpanel(req):
    
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        return render(req, 'adminpanel.html', {'data': data})

    
    elif 'user_id' in req.session:
        user = Student.objects.get(id=req.session['user_id'])
        data = {
            'name': user.name,
            'email': user.email,
            'contact': user.contact,
        }
        return render(req, 'dashboard.html', {'data': data})

    return redirect('login')

def logout(req):
    if 'admin_e' in req.session:
        req.session.flush()
        return redirect('landing')
    else:
        return redirect('lo')
