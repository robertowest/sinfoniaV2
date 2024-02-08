# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

# authentication
app_name = __package__.split('.')[1]

urlpatterns = [
    path('',          views.LoginRedirect, name='redirect'),
    path('login/',    views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/",   LogoutView.as_view(), name="logout")
]
