from django.urls import path
from apps.recepcion import views

app_name = 'recepcion'

urlpatterns = [
    path('', views.index, name='home'),
]
