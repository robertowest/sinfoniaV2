from crispy_forms import bootstrap, helper, layout
from django import forms
from django_filters import FilterSet, CharFilter

from .models import Persona


class PersonaFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    apellido = CharFilter(label='Apellido', lookup_expr='icontains')
    documento = CharFilter(label='DNI', lookup_expr='icontains')

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'active']


class PersonaFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><i class="fas fa-filter mr-1"></i><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="/persona/listado/"><i class="fa fa-undo" aria-hidden="true" mr-1></i><span class="text">Limpiar</span></a>'
                                            
        self.layout = layout.Layout(
            layout.Row(
                layout.Div('nombre', css_class='col-lg-4 col-md-4 col-sm-6 mb-0'),
                layout.Div('apellido', css_class='col-lg-4 col-md-4 col-sm-6 mb-0'),
                layout.Div('documento', css_class='col-lg-2 col-md-2 col-sm-6 mb-0'),
                layout.Div('active', css_class='col-lg-2 col-md-2 col-sm-6 mb-0'),
            ),
            layout.Row(
                layout.HTML(bFilter),
                layout.HTML(bLimpiar),
                css_class="float-right",
            ),
        )


# class PersonaFilterForm(helper.FormHelper):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.form_method = 'get'

#         bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter mr-1"></i></span><span class="text">Filtrar</span></button>'
#         bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="/persona/listado/"><span class="icon text-white-50"><i class="fas fa-undo mr-1"></i></span><span class="text">Limpiar</span></a>'

#         self.layout = layout.Layout(
#             layout.Div(
#                 layout.Row(
#                     layout.Div(
#                         layout.Row(
#                             layout.Column('nombre', css_class='col-lg-4 col-md-4 col-sm-12 mb-0'),
#                             layout.Column('apellido', css_class='col-lg-4 col-md-4 col-sm-12 mb-0'),
#                             layout.Column('documento', css_class='col-lg-3 col-md-3 col-sm-6 mb-0'),
#                             layout.Column('active', css_class='col-lg-1 col-md-1 col-sm-3 mb-0'),
#                         ),
#                         css_class="col-lg-12 col-md-12 col-sm-12",
#                     ),
#                     layout.Div(
#                         layout.HTML(bFilter),
#                         layout.HTML(bLimpiar),
#                         css_class="col-12 text-right",
#                     ),
#                 )
#             )
#         )
