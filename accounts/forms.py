from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Availability



class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = CustomUser 
        fields = ( 
            "username", 
            "email",
            "courses",
        )  # new 
 
 
class CustomUserChangeForm(UserChangeForm): 
    class Meta: 
        model = CustomUser 
        fields = ( 
            "username", 
            "email", 
            "courses",
        )  # new


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ('day', 'time_slot')
        