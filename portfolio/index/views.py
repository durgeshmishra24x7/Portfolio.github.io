from django.shortcuts import render
from django.http import HttpResponse

from index.models import Contact_db

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')
def contact(request):
    if request.method =='POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        purpose= request.POST['Purpose']
        # print(name,email,phone,purpose)
        obj=Contact_db(name=name,email=email,phone=phone,Purpose=purpose)
        obj.save()
    
    
    return render(request,'contact.html')