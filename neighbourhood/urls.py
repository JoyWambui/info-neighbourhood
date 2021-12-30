from django.urls import path
from . import views as app_views


urlpatterns=[
    path('', app_views.landing, name='landing'),
    path('homepage/', app_views.homepage, name='homepage'),
    path('registration/', app_views.registration, name='registration'),
    
    
]