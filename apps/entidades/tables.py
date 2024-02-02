from django.db.models import Q

import django_tables2 as tables

from .models import Persona


class PersonaTable(tables.Table):
    # {% url 'persona:detail' record.pk %}
    # {% url 'persona:update' record.pk %}
    # {% url 'persona:delete' record.pk %}
    ACTIONS = '''
    {% if perms.persona.view_persona %}
    <a href="{{record.get_detail_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.persona.change_persona %} 
    <a href="{{record.get_update_url}}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.persona.delete_persona %} 
    <a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" title="Eliminar" data-toggle="modal" data-target="#confirmDeleteModal" id="deleteButton{{record.id}}"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    # sin confirmación
    # <a href="{{record.get_detail_url}}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    # <a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    
    id = tables.Column(orderable=False) # (linkify=True)
    nombre = tables.Column(order_by=('nombre'))
    documento = tables.Column(orderable=False)
    fecha_nacimiento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)
    
    class Meta:
        model = Persona
        template_name = "django_tables2/bootstrap4.html"
        fields = ['id', 'nombre', 'apellido', 'documento', 
                  'fecha_nacimiento', 'edad', 'active']
        attrs = {"class": "table table-hover"}
