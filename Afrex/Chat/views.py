from django.shortcuts import render, redirect, get_object_or_404

#This module I imported below deals on user authentication during signups and logins and reset passwords functionality.
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm

#this module I imported here is for the date and time rendering, and also to calculate timezone and to give out timing to region irrespective of their countries time.
from datetime import datetime
from django.utils import timezone

# Create your views here.

#This functions below works for the signup page
def sign_up(request):
    
    context = {
            'title': 'Let us get you connected by signing up first!'
            }

    if request.method == 'GET':
        form = RegistrationForm()
        context['form'] = form
        return render(request, 'pages/signup.html', context)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            context['form'] = form
            return render(request, 'pages/signup.html', context)
