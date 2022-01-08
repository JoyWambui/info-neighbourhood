from os import name
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.http import Http404


class NeighbourHood(models.Model):
    name = models.CharField(max_length=50,verbose_name='Neighbourhood Name')
    location = models.CharField(max_length=50,verbose_name='Neighbourhood Location')
    occupants = models.IntegerField(verbose_name='Neighbourhood Occupants', default=0)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    health_dept = models.CharField(validators=[phoneNumberRegex],max_length=16,unique=True,verbose_name='Health Department Contact',help_text='Phone Number Format: +254722399744')
    police_dept = models.CharField(validators=[phoneNumberRegex],max_length=16,unique=True,verbose_name='Police Department Contact',help_text='Phone Number Format: +254722399744')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def create_neighbourhood(self):
        self.save()
    
    @classmethod
    def get_neighbourhoods(cls):
        return cls.objects.all()
    
    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        try:
            return cls.objects.get(pk=neighbourhood_id)
        except NeighbourHood.DoesNotExist:
            return Http404
    
    @classmethod    
    def update_neighbourhood(cls,neighbourhood_id,new_name):
        return NeighbourHood.objects.filter(id=neighbourhood_id).update(name=new_name)
    
    @classmethod    
    def update_occupants(cls,neighbourhood_id,occupant_count):
        return NeighbourHood.objects.filter(id=neighbourhood_id).update(occupants=occupant_count)
    
    @classmethod    
    def delete_neighbourhood(cls,neighbourhood_id):
        return NeighbourHood.objects.filter(id=neighbourhood_id).delete()
    
    def __str__(self):
        return self.name
class Profile(models.Model):
    pass


class Post(models.Model):
    pass

class Business(models.Model):
    pass