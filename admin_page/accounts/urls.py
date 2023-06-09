from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("signup/", signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
