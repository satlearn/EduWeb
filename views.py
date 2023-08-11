from django.shortcuts import render,redirect
from .models import sign
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def contact(request):
    return render(request,'contact.html')


def home1(request):
    return render(request,'home1.html')

def login(request):
    signdata = sign.objects.all()
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']        
        for row in signdata:  
            if row.Username == username and row.Password == password:
                return redirect('home1.html')        
        return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')       
             
       

def signup(request):
    tt = sign()     
    if request.method == 'POST':
        if request.POST.get('Username') and request.POST.get('Email_id') and request.POST.get('Phone_Number') and request.POST.get('Password') and request.POST.get('Password'):                   
           tt.Username = request.POST.get('Username')        
           tt.Email_id = request.POST.get('Email_id')
           tt.Phone_Number = request.POST.get('Phone_Number')
           tt.Password = request.POST.get('Password')
           tt.Confirm_Password = request.POST.get('Password')
           tt.save()
           return redirect('login.html')
    return render(request,'signup.html')


def signup_view(request):
    signdata = sign.objects.all()
    return render(request,'signup_view.html',locals())



