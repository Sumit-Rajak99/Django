"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('base/',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('service/',views.service,name='service'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_department/',views.add_department,name='add_department'),
    path('d_data/',views.d_data,name='d_data'),
    path('all_departments/',views.all_departments,name='all_departments'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('adminpanel/',views.adminpanel,name='adminpanel'),
    path('Employee_data/',views.Employee_data,name='Employee_data'),
    path('all_employees/',views.all_employees,name='all_employees'),
    path('forget/',views.forget,name='forget'),
    path('otp/',views.otp,name='otp'),
    path('newpassword/',views.newpassword,name='newpassword'),
    path('newpass/',views.newpass,name='newpass'),
    path('userpanel/',views.userpanel,name='userpanel'),
    path('query/',views.query,name='query'),
    path('userpanel/show_query/',views.show_query,name='show_query'),
    path('userpanel/emp_query/',views.emp_query,name='emp_query'),
    path('adminpanel/replay_query/<int:pk>/',views.replay_query,name='replay_query'),
    path('adminpanel/replay_query/',views.rep_query,name='rep_query'),
    path('adminpanel/ad_reply/<int:pk>/',views.ad_reply,name='ad_reply'),
    path('userpanel/edit_query/<int:pk>/',views.edit_query,name='edit_query'),
    path('userpanel/update_query/<int:pk>/',views.update_query,name='update_query'), 
    path('userpanel/delete_query/<int:pk>/',views.delete_query,name='delete_query'), 
    path('userpanel/panding_query/',views.panding_query,name='panding_query'),
    path('userpanel/done_query/',views.done_query,name='done_query'),
     
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
]
