from django.urls import path

from apps.home import views


app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name

urlpatterns = [
    # página de inicio
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    # páginas de ejemplo
    path('icons', views.icons, name='icons'),
    path('google', views.google, name='google'),
    path('profile', views.profile, name='profile'),
    path('tables', views.tables, name='tables'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
