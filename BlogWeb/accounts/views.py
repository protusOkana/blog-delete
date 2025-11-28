from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
#login views

# Create your views here.
def userRegistration(request):
    if request.method=='POST':
        username=request.POST.get('userId')
        email=request.POST.get('userEmail')
        firstName=request.POST.get('first_name')
        lastName=request.POST.get('last_name')
        tel=request.POST.get('phoneNo')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')

        if pass1 != pass2:
            messages.error(request,'passwords do not match')
            return redirect('register')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'username already taken')
            return redirect('register')
        
        myuser=CustomUser.objects.create_user(
        username=username,
        email=email,
        fname=firstName,
        lname=lastName,
        phone=tel,
        password=pass1
        ) 


        myuser.save()
        messages.success(request,'Account created successfully')
        return redirect('signin')
    return render(request,'accounts/regist.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('userId')
        password = request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
            messages.error(request,'invalid login credentials') 
            return redirect('signin')
    return render(request,'accounts/login.html')


    re        
            #logout view
def signout_view(request):
    logout(request)
    return redirect('signin')  
