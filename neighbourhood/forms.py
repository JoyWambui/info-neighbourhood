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
    occupants = forms.IntegerField(disabled=True)
    
    class Meta:
        model =   NeighbourHood
        exclude = ['admin']