from django.contrib.auth.models import AbstractUser
from django.db import models 

DAYS_OF_WEEK = [
    ('M', 'Monday'),
    ('T', 'Tuesday'),
    ('W', 'Wednesday'),
    ('TH', 'Thursday'),
    ('F', 'Friday'),
]

class Course(models.Model):
    course_code = models.CharField(max_length=10)

    def __str__(self):
        return self.course_code

    
class CustomUser(AbstractUser): 
    courses = models.ManyToManyField( 'Course', blank=True)

class Availability(models.Model):
    ta = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='slots')
    day = models.CharField(max_length=2, choices=DAYS_OF_WEEK)
    time_slot = models.TimeField()

    def __str__(self):
        return f"{self.ta.username} - {self.get_day_display()} at {self.time_slot}"