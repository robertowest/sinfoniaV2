from django.urls import path

from apps.entidades.views.personaViews import *

# app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name
app_name = 'persona'

urlpatterns = [
    # persona
    path('',                    PersonaTemplateView.as_view(), name='index'),
    path('listado/',            PersonaListView.as_view(),     name='list'),
    path('crear/',              PersonaCreateView.as_view(),   name='create'),
    path('<int:pk>/',           PersonaDetailView.as_view(),   name='detail'),
    path('<int:pk>/modificar/', PersonaUpdateView.as_view(),   name='update'),
    path('<int:pk>/eliminar/',  PersonaDeleteView.as_view(),   name='delete'),
]
