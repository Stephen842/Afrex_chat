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
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'pages/signup.html', {'form': form})
