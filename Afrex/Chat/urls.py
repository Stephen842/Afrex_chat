from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("Signup/", views.sign_up, name="signup"),
    path("Login/", views.login, name="login"),
    path("Logout/", views.logout, name="logout"),
]
