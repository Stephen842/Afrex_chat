from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput

#The following code below is for the form aspect whereby users put in their details during the registration process of their respective account, I had to hardcode the process for easy understanding.
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 50, required = True)
    last_name = forms.CharField(max_length = 50, required = True)
    username = forms.CharField(max_length = 50, required = True)
    email = forms.EmailField(max_length = 50, required = True)
    password1 = forms.CharField(max_length = 25, required = True)
    password2 = forms.CharField(max_length = 25, required = True)
    check = forms.BooleanField(required = True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'check']
