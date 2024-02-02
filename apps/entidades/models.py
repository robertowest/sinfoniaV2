import datetime
from django.db import models

from core.audit.models import Auditable


class Persona(Auditable):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.CharField('DNI', max_length=12, null=True, blank=True, unique=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', blank=True, null=True)

    # configuración para admin
    list_display = ['apellido_nombre', 'documento', 'fecha_nacimiento', 'active']
    list_display_links = ['apellido_nombre']
    search_fields = ['nombre', 'apellido']
    list_filter = []

    class Meta:
        db_table = 'personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.nombre_apellido

    @property
    def edad(self):
        if self.fecha_nacimiento is None:
            return None            
        else:
            from datetime import date
            age = date.today().year - self.fecha_nacimiento.year - ((date.today().month, date.today().day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)) 
            return age

    @property
    def nombre_apellido(self):
        return "%s %s" % (self.nombre, self.apellido)

    @property
    def apellido_nombre(self):
        return "%s, %s" % (self.apellido, self.nombre)
