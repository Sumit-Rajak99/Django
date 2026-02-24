from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from app.models import Data 
import json
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
# Create your views here.

# def landing(req):
    
#     data=Data.objects.all()
#     return render(req,'landing.html',{'data':data})
@csrf_exempt
def data_list(req):
    if req.method=='POST':
        data = req.body
        # print(data)
        # print(type(data))
        p_data = json.loads(data)
        # print(p_data)
        # print(type(p_data))
        n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
        # print(n,e,c,a,sep=',')
        Data.objects.create(name=n,email=e,contact=c,age=a)
        # p_data['msg']="data created successfully"
        # print(p_data)
        d={'msg':'object created successfully.......','data':p_data}
        j_data = json.dumps(d)
        # print(j_data)
        # print(type(j_data))
        return HttpResponse(j_data,content_type='application/json')
            
    emp_data = Data.objects.all()
    print(emp_data)
    p_data = list(emp_data.values())
    print(p_data)
    j_data = json.dumps(p_data)
    print(j_data)
    print(type(j_data))
    return JsonResponse(j_data,safe=False)




def detail(req,pk):
    user = Data.objects.filter(id=pk)
    if user:
        if req.method=='PUT':
            data = req.body
            p_data = json.loads(data)
            n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
            # if n and e and c and a:
            if 'name' in p_data and 'email' in p_data and 'contact' in p_data and 'age' in p_data:
                old_obj = Data.objects.get(id=pk)
                old_obj.name = n
                old_obj.email = e 
                old_obj.contact = c
                old_obj.age = a
                old_obj.save()
                d={'msg':'Object updated successfully.........'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')
            else:
                d={'msg':'Some required filelds are missing'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')

        elif req.method=='PATCH':
            data = req.body
            p_data = json.loads(data)
            if p_data:
                # p_data = json.loads(data)
                n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
                old_obj = Data.objects.get(id=pk)
                if 'name' in p_data:
                    old_obj.name = n
                if 'email' in p_data:
                    old_obj.email = e
                if 'contact' in p_data:
                    old_obj.contact = c
                if 'age' in p_data:
                    old_obj.age = a
                old_obj.save()
                d={'msg':'Object partially updated successfully.........'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')
            else:
                d={'msg':'We need atleast one field to update but we don"t provide '}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')

        elif req.method=='DELETE':
            old_obj = Data.objects.get(id=pk)
            old_obj.delete()
            d={'msg':'Object deleted successfully........!'}
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
        emp_data = Data.objects.get(id=pk)
        p_data = model_to_dict(emp_data)
        j_data = json.dumps(p_data)

        return HttpResponse(j_data,content_type='application/json')
    else:
        d={'msg':'Given id is not present in our database'}
        j_data = json.dumps(d)
        return HttpResponse(j_data,content_type='application/json')
    
@csrf_exempt   
def data(req):
    j_data = req.body 
    p_data = json.loads(j_data)
    print(p_data)
    print('id' in p_data)

    if 'id' in p_data:
        oid = p_data.get('id')
        obj_data = Data.objects.filter(id=oid) 
        if obj_data:
            if req.method=='PUT':
                pk=p_data.get('id')
                n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
                # if n and e and c and a:
                if 'name' in p_data and 'email' in p_data and 'contact' in p_data and 'age' in p_data:
                    old_obj = Data.objects.get(id=pk)
                    old_obj.name = n
                    old_obj.email = e 
                    old_obj.contact = c
                    old_obj.age = a
                    old_obj.save()
                    d={'msg':'Object updated successfully.........'}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')
                else:
                    d={'msg':'Some required filelds are missing'}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')

            elif req.method=='PATCH':
                if p_data:
                    pk=p_data.get('id')
                    # p_data = json.loads(data)
                    n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
                    old_obj = Data.objects.get(id=pk)
                    if 'name' in p_data:
                        old_obj.name = n
                    if 'email' in p_data:
                        old_obj.email = e
                    if 'contact' in p_data:
                        old_obj.contact = c
                    if 'age' in p_data:
                        old_obj.age = a
                    old_obj.save()
                    d={'msg':'Object partially updated successfully.........'}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')
                else:
                    d={'msg':'We need atleast one field to update but we don"t provide '}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')

            elif req.method=='DELETE':
                pk=p_data.get('id')
                old_obj = Data.objects.get(id=pk)
                old_obj.delete()
                d={'msg':'Object deleted successfully........!'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')
            
            pk=p_data.get('id')
            emp_data = Data.objects.get(id=pk)
            p_data = model_to_dict(emp_data)
            j_data = json.dumps(p_data)
            return HttpResponse(j_data,content_type='application/json')
        else:
            d={'msg':'Object not present in our database..........'}
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
            
    else:
        if req.method=='POST':
            if 'name' in p_data and 'email' in p_data and 'age' in p_data and 'contact' in p_data: 
                n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
                Data.objects.create(name=n,email=e,contact=c,age=a)
                d={'msg':'object created successfully.......','data':p_data}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')  
            else:
                d={'msg':'Some required fields are missing............'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json') 
        emp_data = Data.objects.all()
        p_data = list(emp_data.values())
        j_data = json.dumps(p_data)
        return HttpResponse(j_data,content_type='application/json') 
        