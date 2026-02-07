from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student,Department,Employee,password,Query
from django.contrib import messages
import random
from django.views.decorators.cache import never_cache


# Create your views here.

def base(req):
    return render(req,'base.html')
def landing(req):
    if 'admin_e' in req.session or 'user_id' in req.session:
        if 'admin_e' in req.session:
            data = {
                'email': req.session['admin_e'],
                'name': req.session['admin_n']
            }
            return render(req, 'adminpanel.html', {'data': data})
        elif 'user_id' in req.session:
            u_id=req.session.get('user_id')
            userdata=Employee.objects.get(id=u_id)
            data={
                'name':userdata.name,
                'email':userdata.email,
                'contact':userdata.contact,
                'department':userdata.department
            }
            
            return render(req,'userpanel.html',{'data':data})
    return render(req,'landing.html')

def home(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        return render(req, 'home.html', {'data': data})
    return render(req,'home.html')

def service(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        return render(req, 'service.html', {'data': data})
    return render(req,'service.html')

def about(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        return render(req, 'about.html', {'data': data})
    return render(req,'about.html')

def contact(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        return render(req, 'contact.html', {'data': data})
    return render(req,'contact.html')

@never_cache             
def login(req):
    # print(req.method)
    if 'admin_e' in req.session or 'user_id' in req.session:
        if 'admin_e' in req.session:
            data = {
                'email': req.session['admin_e'],
                'name': req.session['admin_n']
            }
            return render(req, 'adminpanel.html', {'data': data})
        elif 'user_id' in req.session:
            u_id=req.session.get('user_id')
            userdata=Employee.objects.get(id=u_id)
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

            
            user = Employee.objects.filter(email=e)
            print(user)
            if user:
                userdata=Employee.objects.get(email=e)
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


@never_cache
def adminpanel(req):
    if 'admin_e' in req.session or 'user_id' in req.session:
        
        if 'admin_e' in req.session:
            data = {
                'email': req.session['admin_e'],
                'name': req.session['admin_n']
            }
            if 'q_id' in req.session:
                id = req.session.get('q_id')
                q_data = Query.objects.get(id=id)
                return render(req, 'adminpanel.html', {'data': data,'data1':q_data})
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

@never_cache
def logout(req):
    if 'admin_e' in req.session or 'user_id' in req.session:
        req.session.flush()

        return redirect('login')
    return redirect('login')
        

@never_cache    
def add_department(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        return render(req, 'adminpanel.html', {'data': data,'add_department':'add_department'})
    
    return redirect('login') 

@never_cache   
def d_data(req):
    if req.method=='POST':
        n=req.POST.get('d_name')
        h=req.POST.get('d_head')
        d_data=Department.objects.filter(d_name=n)
        if not d_data:
            Department.objects.create(d_name=n,d_head=h)
            return redirect('add_department')
        else:
            return redirect('add_department')           
    
    return redirect('login') 

   
@never_cache
def add_employee(req):
    if 'admin_e' not in req.session:
        return redirect('login')

    a_data = {
        'email': req.session['admin_e'],
        'name': req.session['admin_n']
    }
    deptdata = Employee.objects.all()
    dep=Department.objects.all()
    if req.method == "POST":
        name = req.POST['name']
        email = req.POST['email']
        contact = req.POST['contact']
        department = req.POST['dept']
        
        user=Employee.objects.filter(email=email)
        
        if user:
            messages.error(req,'email already exites here')
        
        else:
            Employee.objects.create(
            name=name,
            email=email,
            contact=contact,
            department=department
        )
            send_mail(
            "django from here",
            f'email:{email}\n name:{name}\n contact use like password {contact}\n department:{department}\n',
        
            "sumitrajaksumitrajak793@gmail.com",
            [email],
            fail_silently=False,
            )
            return render(req, 'adminpanel.html', {
                'data': a_data,
                'add_employee': True,
                'deptdata': deptdata,
                'dep': dep})
        
    return render(req, 'adminpanel.html', {
        'data': a_data,
        'add_employee': True,
        'deptdata': deptdata,
        'dep':dep
    })
    
    
@never_cache   
def all_departments(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        depdata=Department.objects.all()
        
        print(depdata.values())
        return render(req, 'adminpanel.html',{'all_department':True ,'depdata':depdata})
    
    return redirect('login')  
    
@never_cache    
def Employee_data(req):
    if req.method=='POST':
        n=req.POST.get('name')
        c=req.POST.get('contact')
        e=req.POST.get('email')
        d=req.POST.get('dept')      
        d_data=Employee.objects.filter(d_name=n)
        if not d_data:
            Employee.objects.create(name=n,contact=c,email=e,Dept=d)
            return redirect('add_employee')
        else:
             return redirect('add_employee')
    return redirect('login') 

@never_cache
def all_employees(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        data1=Employee.objects.all()
        print("Hello........")
        print(data1.values())
        return render(req, 'adminpanel.html',{'all_employees':True ,'data': data,'data1':data1})
    return redirect('login')

# forget password start form here -----------------------------------------------------------------------------------
@never_cache
def forget(req):
    return render(req,'forget.html')

@never_cache
def otp(req):
    if req.method=='POST':
        email=req.POST.get('email')
        otp_code=random.randint(111111,999999)
        req.session['email']=email
        req.session['oyp']=otp_code
        send_mail(
            subject="Forget password",
            message=f'User Email OTP: {otp_code}',
            from_email="sumitrajaksumitrajak793@gmail.com",  
            recipient_list=[email],
            fail_silently=False,
        )
        return render(req,'otp.html') 
    return render(req,'otp.html')


@never_cache
def newpassword(req):
    if req.method=='POST':
        user_otp=req.POST.get('otp')
        store_otp=req.POST.get('otp')
        
        if str(user_otp)==str(store_otp):
            email=req.session.get('email')
            return render(req,'newpassword.html',{'email':email})
        
        else:
            return render(req, 'otp.html', {'error': 'Invalid OTP'})
        
    email = req.session.get('email')
    return render(req,'newpassword.html',{'email':email})


@never_cache
def newpass(req):
    if req.method=='POST':
        e = req.POST.get('email')
        p = req.POST.get('npass')
        cp = req.POST.get('cnpass')
        if p == cp:
            userdata = Employee.objects.get(email=e)
            userdata.contact=p
            userdata.save()
            messages.info(req,'Password reset successfully')
            return redirect('landing')
        else:
            messages.info(req,'Password and conform password not matched')
            return redirect('newpassword')
    return redirect('login')
    
# userpanel start from here ---------------------------------------------------------
@never_cache
def userpanel(req):
    if 'user_id' in req.session:
        u_id=req.session.get('user_id')
        userdata=Employee.objects.get(id=u_id)
        data={
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'department':userdata.department
        }
        
        return render(req,'userpanel.html',{'data':data})
       
    else:
        return redirect('login') 
    
          
@never_cache
def query(req):
    if 'user_id' in req.session:
        u_id = req.session.get('user_id')
        userdata = Employee.objects.get(id=u_id)

        data = {
            'name': userdata.name,
            'email': userdata.email,
            'contact': userdata.contact,
            'department': userdata.department
        }
    
        if req.method == 'POST':
            name = req.POST.get('name')
            email = req.POST.get('email')
            user_query = req.POST.get('query')
            department = req.POST.get('department')

            Query.objects.create(
                Name=name,
                Email=email,
                Query=user_query,
                Department=department,
            )

            return redirect('userpanel')
        all_department=Department.objects.all()
        return render(req, 'userpanel.html', {'data': data,'query':all_department})
    
    return redirect('login')


@never_cache
def show_query(req):
    if 'user_id' in req.session:
        id = req.session.get('user_id')
        userdata = Employee.objects.get(id=id)
        data={
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'department':userdata.department
        }
        emp_query=Query.objects.filter(Email=userdata.email)
        return render(req,'userpanel.html',{'data':data,'data1':emp_query})

    return redirect('login')

@never_cache
def emp_query(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        all_query=Query.objects.all() 
        return render(req, 'adminpanel.html',{'data': data,'emp_query':all_query})
    
    return redirect('login')

@never_cache
def replay_query(req,pk):
    if 'admin_e' in req.session:
        req.session['q_id']=pk
        return redirect('adminpanel')
    return render(req,'replay_query.html')

@never_cache
def rep_query(req):
    if 'admin_e' in req.session:
        data = {
            'email': req.session['admin_e'],
            'name': req.session['admin_n']
        }
        pk=req.session['q_id']
        q_data=Query.objects.get(id=pk)
        return render(req, 'replay_query.html',{'data': data,'data1':q_data})
    return redirect('login')


@never_cache
def ad_reply(req,pk):
    if 'admin_e' in req.session:
        if req.method=='POST':
            ad=req.POST.get('admin_reply')
            print(ad)
            if ad: 
                old_data=Query.objects.get(id=pk)
                old_data.Admin_replay=ad
                old_data.Status='done'
                old_data.save()
                return redirect('emp_query')
            
    return redirect('login')


@never_cache           
def edit_query(req,pk):
    if 'user_id' in req.session:
        id = req.session.get('user_id')
        userdata = Employee.objects.get(id=id)
        data={
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'department':userdata.department
        }
        q_data=Query.objects.get(id=pk)
        return render(req, 'userpanel.html',{'data': data,'data2':q_data})
    return redirect('login')


@never_cache        
def update_query(req,pk):
    if 'user_id' in req.session:
        id = req.session.get('user_id')
        userdata = Employee.objects.get(id=id)
        data={
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'department':userdata.department
        }
        old_q_data=Query.objects.get(id=pk)
        old_q_data.Query=req.POST.get('query')
        old_q_data.save()
        emp_query=Query.objects.filter(Email=userdata.email)
        return render(req,'userpanel.html',{'data':data,'data1':emp_query})
    return redirect('login')

@never_cache
def delete_query(req,pk):
    if 'user_id' in req.session:
        id = req.session.get('user_id')
        userdata = Employee.objects.get(id=id)
        data={
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'department':userdata.department
        }
        q_data=Query.objects.get(id=pk)
        q_data.delete()
        emp_query=Query.objects.filter(Email=userdata.email)
        return render(req,'userpanel.html',{'data':data,'data1':emp_query})
    return redirect('login')

@never_cache        
def panding_query(req):
    if 'user_id' in req.session:
        id = req.session.get('user_id')
        userdata = Employee.objects.get(id=id)
        data={
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'department':userdata.department
        }
        query=Query.objects.filter(Email=userdata.email,Status='pending')
        return render(req,'userpanel.html',{'data':data,'panding_query': query})
    return redirect('login')

@never_cache    
def done_query(req):
    if 'user_id' in req.session:
        id = req.session.get('user_id')
        userdata = Employee.objects.get(id=id)
        data={
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'department':userdata.department
        }
        query=Query.objects.filter(Email=userdata.email,Status='done')
        return render(req,'userpanel.html',{'data':data,'panding_query': query})
    return redirect('login')
        
        
    
            
    

    
