#forms: trae las herramientas de Django para construir formularios
from django import forms
# Servicio: el modelo de la Unidad 2, importado desde este mismo directorio
from .models import Servicio

# class ServicioForm: un formulario generado automáticamente a partir del modelo Servicio
class ServicioForm(forms.ModelForm):
    # Meta: clase interna donde le dices a Django de qué modelo y qué campos generar
    class Meta:
        # model: el modelo del que se generan los campos del formulario
        model = Servicio
        # fields: lista de campos del modelo que sí aparecen en el formulario
        # "propietario" queda fuera a propósito: lo asigna la vista, no el usuario
        fields = ['titulo', 'descripcion', 'precio', 'categoria']