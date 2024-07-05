from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput


# The following code below is for the form aspect whereby users put in their details during the registration process of their respective account, I had to hardcode the process for easy understanding.
class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    lastname = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )

    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    password1 = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )

    password2 = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Confirm Password"}
        ),
    )

    check = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "check",
        ]


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    password = forms.CharField(
        max_length=25,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
