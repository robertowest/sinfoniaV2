from crispy_forms import helper, layout
from django import forms

from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'fecha_nacimiento', 'active']
        widgets = {
            'documento': forms.TextInput(attrs={'placeholder': '20.123.456'}),
            'fecha_nacimiento': forms.TextInput(attrs={'placeholder': '31/03/1990'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts
        self.helper.layout = layout.Layout()

        # # agregamos todos los campos
        # for fld in self.Meta.fields:
        #     self.helper.layout.append(fld)

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            layout.Row(
                layout.Column('nombre', css_class='col-lg-6 col-md-6 mb-0'),
                layout.Column('apellido', css_class='col-lg-6 col-md-6 mb-0'),
            ),
            layout.Row(
                layout.Column('documento', css_class='col-lg-6 col-md-6 mb-0'),
                layout.Column('fecha_nacimiento', css_class='col-lg-6 col-md-6 mb-0'),
            ),
            'active',
        )

        # agregamos los botones de acción
        bSave = '<button type="submit" class="btn btn-success btn-icon-split mr-2"><i class="fas fa-save"></i><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-warning btn-icon-split" href="{{request.META.HTTP_REFERER}}"><i class="fas fa-undo"></i><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))
