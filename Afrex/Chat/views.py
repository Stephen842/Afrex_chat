from django.shortcuts import render, redirect, get_object_or_404

# This module I imported below deals on user authentication during signups and logins and reset passwords functionality.
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

# this module I imported here is for the date and time rendering, and also to calculate timezone and to give out timing to region irrespective of their countries time.
from datetime import datetime
from django.utils import timezone

# Create your views here.


# This functions below handles the logic behind the signup page for users registration
def sign_up(request):

    context = {"title": "Let us get you connected by signing up first!"}

    if request.method == "GET":
        form = RegistrationForm()
        context["form"] = form
        return render(request, "pages/signup.html", context)

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # Specify the authentication backend explicitly
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home")
        else:
            context["form"] = form
            return render(request, "pages/signup.html", context)


# This function below is meant for handling the logic behind users login procedures
def sign_in(request):
    context = {"title": "Sign in to get connected"}

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        context["form"] = form
        return render(request, "pages/signin.html", context)

    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"].lower()
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")

        messages.error(
            request,
            f"The email address or password you entered is incorrect. Please try again.",
        )
        context["form"] = form
        return render(request, "pages/signin.html", context)

def sign_out(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    context = {
        'title': 'Afrex Chat System - Real Time Communication Across Africa'
    }
    return render(request, 'pages/home.html', context)

def terms(request):
    context = {
        'title': 'Afrex Terms & Conditions'
    }
    return render(request, 'pages/Terms_Condition.html', context)