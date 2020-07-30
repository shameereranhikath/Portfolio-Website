from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.


def home(request):
    context={}
    return render(request,'home.html',context)

def aboutus(request):
    context={}
    return render(request,'about.html',context)

def projects(request):
    context={}
    return render(request,'project.html',context)

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        # print('ssssssss')
        comments=request.POST['comments']
        data=Contact(name=name,email=email,phone=phone,comment=comments)
        data.save()
        # print(comments)
        return redirect('/')
    else:
        context={}
        print('this is get')
        return render(request,'contact.html',context)