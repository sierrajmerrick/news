from django.contrib.auth.models import AbstractUser
from django.db import models 

class CustomUser(AbstractUser): 
    availability = models.DateTimeField(null=True, blank=True)    