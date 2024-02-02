from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import views


app_name = 'registration'

urlpatterns = [
    # path('login/',    LoginView.as_view, name='login'),
    path('login/',    views.login_view, name='login'),
    path('logout/',   LogoutView.as_view(), name='logout'),

    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
]
