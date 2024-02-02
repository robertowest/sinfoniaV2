from django.urls import path
from . import views

app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name

urlpatterns = [
    # persona
    path('persona/', views.PersonaTemplateView.as_view(), name='persona_index'),
    path('persona/listado/', views.PersonaListView.as_view(), name='persona_list'),
    path('persona/crear/', views.PersonaCreateView.as_view(), name='persona_create'),
    path('persona/<int:pk>/', views.PersonaDetailView.as_view(), name='persona_detail'),
    path('persona/<int:pk>/modificar/', views.PersonaUpdateView.as_view(), name='persona_update'),
    path('persona/<int:pk>/eliminar/', views.PersonaDeleteView.as_view(), name='persona_delete'),
]
