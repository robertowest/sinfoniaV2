from django.urls import path
from apps.recepcion import views


app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name

urlpatterns = [
    path('', views.index, name='index'),
    path('remesas/', views.obtener_remesas, name='remesas'),
]
