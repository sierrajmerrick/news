from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
 
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Availability
 
 
class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm 
    model = CustomUser 
    list_display = [ 
        "email", 
        "username",
        "is_staff", 
    ] 

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("courses",)}),) 
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("courses",)}),) 
 
 
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Course)
admin.site.register(Availability)