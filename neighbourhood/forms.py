from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(UserCreationForm):
    first_name= forms.CharField(label='First Name' ,error_messages={'required': 'Please enter your first name'})
    last_name= forms.CharField(label='Last Name',error_messages={'required': 'Please enter your last name'})
    email= forms.EmailField(label='Email Address' ,help_text='Format: 123@gmail.com, 456@yahoo.com',error_messages={'required': 'Please enter your email address'})
    
    class Meta:
        model= User
        fields=['first_name','last_name','username','email','password1','password2']

class NeighbourHoodCreationForm(forms.ModelForm):
    
    class Meta:
        model =   NeighbourHood
        exclude = ['admin','occupants']
        
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='Your First name', max_length=50, required=True)
    last_name = forms.CharField(label='Your Last name', max_length=50, required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['profile_user']

class BusinessCreationForm(forms.ModelForm):
    
    class Meta:
        model =   Business
        exclude = ['business_owner']

class PostCreationForm(forms.ModelForm):
    
    class Meta:
        model =   Post
        exclude = ['post_owner','post_creation']
