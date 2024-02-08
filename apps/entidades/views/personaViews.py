from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator
# from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from core.audit.views  import AuditableMixin
from core.common.utils import PagedFilteredTableView

from apps.entidades.models  import Persona
from apps.entidades.tables  import PersonaTable
from apps.entidades.filters import PersonaFilter, PersonaFilterForm
from apps.entidades.forms   import PersonaForm


class PersonaTemplateView(generic.TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return PersonaListView.as_view()(request)


class PersonaListView(PagedFilteredTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    model = Persona
    table_class = PersonaTable              # SingleTableView
    filter_class = PersonaFilter            # PagedFilteredTableView
    formhelper_class = PersonaFilterForm    # PagedFilteredTableView
    template_name = 'common/tabla.html'

    # # usando select_related
    # Conductores = Conductor.objects.values('pk', 'Nombre', 'Apellidos', 'Empresa__Nombre',
    #     'Usuario__username', 'SituacionFrontend', 'SituacionBackend', 'Baja'
    # ).select_related('Usuario', 'Empresa').all().order_by('-pk')

    # def get_queryset(self):
    #     # return models.Persona.objects.filter(active=True)
    #     # eliminamos las personas que son comerciales de la empresa
    #     inner_qs = Comercial.objects.all()
    #     obj_list = models.Persona.objects.exclude(id__in=inner_qs) \
    #                     .filter(active=True).order_by('nombre', 'apellido')
    #     return obj_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            from django.contrib.auth.models import Permission
            from django.contrib.contenttypes.models import ContentType
            content_type = ContentType.objects.get_for_model(Persona)
            # add, change, delete, view & custom
            if Permission.objects.get(codename="add_persona", content_type=content_type):
                context["add_permission"] = True
        return context


class PersonaDetailView(PermissionRequiredMixin, generic.DetailView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    model = Persona
    permission_required = '{domain}/view_{app}'.format(domain='persona', app='persona')
    # template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())
    template_name = 'comunes/detalle_modal.html'


class PersonaCreateView(AuditableMixin, PermissionRequiredMixin, generic.CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    model = Persona
    permission_required = '{domain}/add_{app}'.format(domain='persona', app='persona')
    form_class = PersonaForm
    template_name = 'comunes/formulario.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object'] = self.model  # IMPORTANTE: pasamos el modelo como object
    #     return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class PersonaUpdateView(AuditableMixin, PermissionRequiredMixin, generic.UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    model = Persona
    permission_required = '{domain}/change_{app}'.format(domain='persona', app='persona')
    form_class = PersonaForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class PersonaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    model = Persona
    permission_required = '{domain}/del_{app}'.format(domain='persona', app='persona')
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        #reverse_lazy('persona:detail', args=(self.object.pk,))
        return reverse_lazy('persona:list')
