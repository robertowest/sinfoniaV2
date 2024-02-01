from django.urls import path
from apps.home import views

app_name = 'home'

urlpatterns = [
    # página de inicio
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    # páginas de ejemplo
    path('dashboard', views.dashboard, name='dashboard'),
    path('icons', views.icons, name='icons'),
    path('google', views.google, name='google'),
    path('profile', views.profile, name='profile'),
    path('tables', views.tables, name='tables'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
