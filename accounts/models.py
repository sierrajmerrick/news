from django.contrib.auth.models import AbstractUser
from django.db import models 

class CustomUser(AbstractUser): 
    availability = models.TimeField(null=True, blank=True)
    day = models.CharField(null=True, blank=True)