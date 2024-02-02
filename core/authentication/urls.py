from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import login_view, register_user, LoginRedirect

app_name = 'authentication'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', LoginRedirect, name='redirect'),
]
