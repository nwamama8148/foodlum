from django.shortcuts import render, HttpResponse, redirect
from .forms import ReservationForm, RegistrationForm
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import UserCreationForm



# Create your views here.


def index(request):
    form = ReservationForm()
    is_best = FoodProduct.objects.all()
    is_lunch = FoodProduct.objects.filter(is_lunch =True)
    is_breakfast = FoodProduct.objects.filter(is_breakfast =True)
    is_dinner = FoodProduct.objects.filter(is_dinner =True)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Reservation submitted successfully')
            return redirect('index')
        else:
            messages.error(request, 'error bound')
   
    return render(request, 'base.html', {
        'form':form,
        'is_best':is_best,
        'is_lunch': is_lunch,
        'is_breakfast': is_breakfast,
        'is_dinner': is_dinner,
        } )

def about_page(request):
    return render(request, 'about_page.html')

def services_page(request):
    return render(request, 'services_page.html')

def signup(request):
    user = RegistrationForm()
    if request.method == 'POST':
        user = RegistrationForm(request.POST)
        if user.is_valid():
            user.save()
            user = auth
            messages.success(request, 'Credentials were successfully obtained !!!')
            return redirect('index')
    else:
        user = RegistrationForm()
        messages.error(request, 'An error occurred')
    return render(request, 'signup.html', {
        'user': user,
    })

