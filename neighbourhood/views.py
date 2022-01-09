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
            messages.success(request, 'Account created successfully!')
            return redirect('homepage')
            
    else:
        form= RegistrationForm()
    title='Create New Account'
    context = {
        'form' : form,
        'title' : title,
    } 
    if request.user.is_authenticated:
        return redirect('homepage')
   
    return render(request, 'registration/registration.html', context)        

    
@login_required(login_url='login')
def homepage(request):
    profile= Profile.get_profile(request.user.id)
    user_neighbourhood = 'None'
    posts=[]
    try:
        user_neighbourhood = NeighbourHood.find_neighbourhood(profile.neighbourhood.id)
        posts = user_neighbourhood.post_neighbourhood.all()
        occupants = user_neighbourhood.user_neighbourhood.all().count()

    except AttributeError:
        messages.error(request,('Update your Profile to view your neighbourhood information.'))
    # businesses = user_neighbourhood.neighbourhood_business.all()
    
    #post creation
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_owner = request.user
            post.save()
            messages.success(request,('Post successfully created'))
        else:
            messages.error(request,('An error occured while saving the form'))
        return redirect('homepage')
    else:
        form= PostCreationForm()
    context = {
        'form': form,
        'user_neighbourhood': user_neighbourhood,
        'posts': posts,
        'occupants': occupants,
    }

    return render(request,'homepage.html',context)

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
    occupants = neighbourhood.user_neighbourhood.all().count()
    if request.method == 'POST':
        form = NeighbourHoodCreationForm(request.POST, instance=neighbourhood)

        if form.is_valid():
            form.save()
            return redirect('single_neighbourhood' ,id=id)
    else:
        form = NeighbourHoodCreationForm(instance=neighbourhood)
    
    title = 'Neighbourhood Details'
    context = {
        'neighbourhood': neighbourhood,
        'title': title,
        'occupants': occupants,
        'form':form,
    }
    return render(request,'single_neighbourhood.html',context)

@login_required(login_url='login')
def delete_neighbourhood(request, id):
    NeighbourHood.delete_neighbourhood(id)
    return redirect('neighbourhoods')


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
            business.business_owner = request.user
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

@login_required(login_url='login')
def search_business(request):
    profile= Profile.get_profile(request.user.id)
    user_neighbourhood = NeighbourHood.find_neighbourhood(profile.neighbourhood.id)
    businesses = []
    if 'search_form' in request.GET and request.GET["search_form"]:
        query = request.GET.get('search_form')
        if query=='':
            query =='None'
        businesses = user_neighbourhood.neighbourhood_business.filter(business_name__icontains=query)
        
        title='Search Results'
        context ={
            'title':title,
            'businesses': businesses,
            'query': query,
            'user_neighbourhood': user_neighbourhood,
        }
        return render(request, 'search.html', context) 
    
@login_required(login_url='login')
def businesses(request):
    profile= Profile.get_profile(request.user.id)
    user_neighbourhood = None
    businesses=[]
    try:
        user_neighbourhood = NeighbourHood.find_neighbourhood(profile.neighbourhood.id)
        businesses = user_neighbourhood.neighbourhood_business.all()

    except AttributeError:
        messages.error(request,('Update your Profile to view your businesses in your neighbourhood.'))

    title = 'Businesses'
    context = {
        'businesses': businesses,
        'title': title,
        'user_neighbourhood':user_neighbourhood,
    }
    return render(request,'businesses.html',context)
         