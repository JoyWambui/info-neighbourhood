from django.urls import path
from . import views


urlpatterns=[
    path('', views.landing, name='landing'),
    path('homepage/', views.homepage, name='homepage'),
    path('registration/', views.registration, name='registration'),
    path('neighbourhoods/', views.neighbourhoods, name='neighbourhoods'),
    path('neighbourhoods/create/', views.create_neighbourhood, name='create_neighbourhood'),
    path('neighbourhoods/<int:id>/', views.single_neighbourhood, name='single_neighbourhood'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('businesses/register/', views.register_business, name='register_business'),
    path('businesses/search/', views.search_business, name='search_business'),

]