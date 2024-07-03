from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
]
