from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import *


def registration(request):
    '''View function to register new users'''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            subject = 'Welcome to INFO-NEIGHBOURHOOD!'
            message = f'Hi {user.first_name}\nInfo-Neighbourhood would like to officially welcome you to our growing community. Find out all you need concerning your neighbourhood, see what your neighbours are up to, and share information with your neighbours.\nRemember to enjoy the app!\n\nKind Regards,\nInfo-Neighbourhood Management.'
            email_from = settings.EMAIL_HOST_USER
            recepient_list = [user.email,]
            send_mail(subject,message,email_from,recepient_list)
            messages.success(request, 'Account created successfully! Check your email for a welcome mail.')
            return redirect('homepage')
            
    else:
        form= RegistrationForm()
    title='Create New Account'
    context = {
        'form' : form,
        'title' : title,
    }    
    return render(request, 'registration/registration.html', context)        

def landing(request):
    return render(request,'landing.html')
    

def homepage(request):
    return render(request,'homepage.html')
