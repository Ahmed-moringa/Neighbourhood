from re import T
from unicodedata import name
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Neighbourhood(models.Model):
    name = models.CharField(max_length=60, blank=True)
    location = models.CharField(max_length=60, blank=True)
    occupants = models.CharField(max_length=10, blank=True)
    # admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='neighbourhood' )
    
    def __str__(self):
        return self.name()

class User(models.Model):
     name = models.CharField(max_length=60, blank=True)
     id = models.CharField(max_length=10, blank=True,primary_key=True)
     neighbour_identificaion = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbourhood_id')
     email = models.EmailField()

     def __str__(self):
        return self.name()

class Buisness(models.Model):
    name = models.CharField(max_length=60, blank=True)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbourhood' )
    neighbour_identification = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbourhood_id')
    
    def __str__(self):
        return self.name()