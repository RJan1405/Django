# accounts/urls.py

from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
# This file defines the URL patterns for the accounts app, including a path for user signup.