from django.shortcuts import render
from app.models import Student,Aadhar

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def forword_access(req):
    # # without related_name
    # stu_data=Student.objects.all()
    # print(stu_data.query)
    # print(list(stu_data))
    # for i in stu_data:
    #     print(i.name,i.email,i.contact,i.city,i.aadhar_no.aadhar_no,i.aadhar_no.create_date,i.aadhar_no.create_by)
    # return render(req,'landing.html',{'stu_data':stu_data})
    
    # # with related_name
    # stu_data=Student.objects.all()
    # for i in stu_data:
    #     print(i.name,i.email,i.contact,i.city,i.aadhar_no.aadhar_no,i.aadhar_no.create_date,i.aadhar_no.create_by)
    # return render(req,'landing.html',{'stu_data':stu_data})

    # with select_related()
    stu_data=Student.objects.select_related('aadhar_no')
    print(stu_data.query)
    print(list(stu_data))
    for i in stu_data:
        print(i.name,i.email,i.contact,i.city,i.aadhar_no.aadhar_no,i.aadhar_no.create_date,i.aadhar_no.create_by)
    return render(req,'landing.html',{'stu_data':stu_data})

def reverse_access(req):
    # # without related_name
    # a_data=Aadhar.objects.all()
    # for i in a_data:
    #     print(i.aadhar_no,i.create_date,i.create_by,i.student.name,i.student.email,
    #           i.student.contact,i.student.city) 
    # return render(req,'landing.html',{'a_data':a_data})
    
    # with related_name
    a_data=Aadhar.objects.all()
    for i in a_data:   # related model name in lowercase (student) change into related_name(xyz)
        print(i.aadhar_no,i.create_date,i.create_by,i.xyz.name,i.xyz.email,
              i.xyz.contact,i.xyz.city) 
    return render(req,'landing.html',{'a_data':a_data})
     
    
