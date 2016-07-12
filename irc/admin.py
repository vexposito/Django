from django.contrib import admin
from .models import FormularioCrear, FormularioParar, FormularioRegistro
from .forms import FormularioCrearForm, FormularioPararForm, FormularioRegistroForm

# Definimos los modelos que tenemos
class AdminFormularioCrear(admin.ModelAdmin):
	list_display = ["__unicode__",  "servidor", "puerto", "canal", "nombre", "patron"]
	form = FormularioCrearForm
	class Meta:
		model = FormularioCrear  # El mismo nombre que ne .models

class AdminFormularioRegistro(admin.ModelAdmin):
	list_display = ["__unicode__",  "nombre", "apellidos", "codigo_postal", "email"]
	form = FormularioRegistroForm
	class Meta:
		model = FormularioRegistro

admin.site.register(FormularioCrear, AdminFormularioCrear) 
admin.site.register(FormularioRegistro, AdminFormularioRegistro)
#18