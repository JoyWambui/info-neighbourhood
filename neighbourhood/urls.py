from django.urls import path
from . import views


urlpatterns=[
    path('', views.landing, name='landing'),
    path('homepage/', views.homepage, name='homepage'),
    path('registration/', views.registration, name='registration'),
    path('neighbourhoods/create', views.create_neighbourhood, name='create_neighbourhood'),
    
]