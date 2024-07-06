from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth


urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
    path('password-reset/', auth.PasswordResetView.as_view(template_name = 'pages/password_reset.html'), name = 'password_reset'),
    path('password-reset/done/', auth.PasswordResetDoneView.as_view(template_name = 'pages/password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(template_name='pages/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', auth.PasswordResetCompleteView.as_view(template_name = 'pages/password_reset_complete.html'), name = 'password_reset_complete'),
]
