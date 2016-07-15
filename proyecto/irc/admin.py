from django.contrib import admin
from .models import FormularioCrear, FormularioParar, FormularioRegistro, FormularioEstado, EVENTOS, MENSAJES, BOT_INFO
from .forms import FormularioCrearForm, FormularioPararForm, FormularioRegistroForm, FormularioEstadoForm, EVENTOSForm, MENSAJESForm, BOT_INFOForm

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

class AdminFormularioParar(admin.ModelAdmin):
	list_display = ["__unicode__",  "ID_BOT"]
	form = FormularioPararForm
	class Meta:
		model = FormularioParar

class AdminFormularioEstado(admin.ModelAdmin):
	list_display = ["__unicode__", "ID_BOT" ]
	form = FormularioEstadoForm
	class Meta:
		model = FormularioEstado

class AdminEVENTOS(admin.ModelAdmin):
	list_display = ["__unicode__", "ID_EVENT", "FECHA", "CANAL", "SERVIDOR", "PATRON"]
	form = EVENTOSForm
	class Meta:
		model = EVENTOS

class AdminMENSAJES(admin.ModelAdmin):
	list_display = ["__unicode__", "ID_MSG", "FECHA", "CANAL", "SERVIDOR", "USUARIO", "MENSAJE"]
	form = MENSAJESForm
	class Meta:
		model = MENSAJES

class AdminBOT_INFO(admin.ModelAdmin):
	list_display = ["__unicode__", "ID_CONVERS", "ID_BOT", "INICIO", "ULTIMA", "SERVIDOR", "CANAL", "EVENTOS", "NUM_MSG", "ESTADO"]
	form = BOT_INFOForm
	class Meta:
		model = BOT_INFO

admin.site.register(FormularioRegistro, AdminFormularioRegistro)
admin.site.register(FormularioParar, AdminFormularioParar) 
admin.site.register(FormularioEstado, AdminFormularioEstado) 
admin.site.register(FormularioCrear, AdminFormularioCrear) 
admin.site.register(EVENTOS, AdminEVENTOS) 
admin.site.register(MENSAJES, AdminMENSAJES) 
admin.site.register(BOT_INFO, AdminBOT_INFO)

#18