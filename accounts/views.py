from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, AvailabilityForm
from .models import Availability, CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home_view(request):
    slots = Availability.objects.all()
    return render(request, 'home.html', {'availabilities': slots})

def ta_detail_view(request, pk):
    ta =get_object_or_404(CustomUser, pk=pk)
    return render(request, 'ta_detail.html', {'ta':ta})

@login_required
def add_hours_view(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.ta = request.user
            slot.save()
            return redirect('home')
    else: 
        form = AvailabilityForm()

    return render(request, 'add_hours.html', {'form': form})
