from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import *

def landing(request):
    return render(request,'landing.html')

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

    
@login_required(login_url='login')
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url='login')
def create_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodCreationForm(request.POST)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user
            neighbourhood.save()
            messages.success(request,('Neighbourhood successfully created'))
        else:
            messages.error(request,('An error occured while saving the form'))
        return redirect('neighbourhoods')
    else:
        form= NeighbourHoodCreationForm()
    title = 'Add Neighbourhood'
    context = {
        'form': form,
        'title': title,
    }
    return render(request,'neighbourhood_create.html',context)

@login_required(login_url='login')
def neighbourhoods(request):
    neighbourhoods = NeighbourHood.get_neighbourhoods(
    )
    title = 'Neighbourhoods'
    context = {
        'neighbourhoods': neighbourhoods,
        'title': title,
    }
    return render(request,'neighbourhoods.html',context)

@login_required(login_url='login')
def single_neighbourhood(request, id):
    neighbourhood = NeighbourHood.find_neighbourhood(id)
    title = 'Neighbourhood Details'
    context = {
        'neighbourhood': neighbourhood,
        'title': title,
    }
    return render(request,'single_neighbourhood.html',context)

@login_required(login_url='login')
def profile(request,id):
    profile = Profile.get_profile(id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile' ,id=id)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    title = 'My Profile'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'title': title,
    }
    return render(request,'profile.html',context)


@login_required(login_url='login')
def register_business(request):
    if request.method == 'POST':
        form = BusinessCreationForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.business_name = request.user
            business.save()
            messages.success(request,('Business successfully registered'))
        else:
            messages.error(request,('An error occured while saving the form'))
        return redirect('homepage')
    else:
        form= BusinessCreationForm()
    title = 'Add Business'
    context = {
        'form': form,
        'title': title,
    }
    return render(request,'business_create.html',context)   