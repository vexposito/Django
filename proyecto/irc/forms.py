from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import FormularioCrear, FormularioParar, FormularioRegistro, FormularioEstado, EVENTOS, MENSAJES, BOT_INFO
# ESTADO, EVENTOS, BOT_INFO 
 
class FormularioRegistroForm(forms.ModelForm):
	class Meta: 
		model = FormularioRegistro
		fields = ["nombre", "apellidos", "email", "codigo_postal"]


class FormularioCrearForm(forms.ModelForm):
	class Meta:
		model = FormularioCrear
		fields = ["servidor", "puerto", "canal", "nombre", "patron"] # Lista de lo que queremos ver en el formulario

class FormularioPararForm(forms.ModelForm):
	class Meta:
		model = FormularioParar
		fields = ["ID_BOT"] # Lista de lo que queremos ver en el formulario

class FormularioEstadoForm(forms.ModelForm):
	class Meta:
		model = FormularioEstado
		fields = ["ID_BOT"] # Lista de lo que queremos ver en el formulario

class EVENTOSForm(forms.ModelForm):
	class Meta:
		model = EVENTOS
		fields = ["ID_EVENT", "FECHA", "CANAL", "SERVIDOR", "PATRON"]# Lista de lo que queremos ver en el formulario

class MENSAJESForm(forms.ModelForm):
	class Meta:
		model = MENSAJES
		fields = ["ID_MSG", "FECHA", "CANAL", "SERVIDOR", "USUARIO", "MENSAJE"]# Lista de lo que queremos ver en el formulario


class BOT_INFOForm(forms.ModelForm):
	class Meta:
		model = BOT_INFO
		fields = ["ID_CONVERS", "ID_BOT", "INICIO", "ULTIMA", "SERVIDOR", "CANAL", "EVENTOS", "NUM_MSG", "ESTADO"]# Lista de lo que queremos ver en el formulario





# class FormularioInicialForm(forms.Form):

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }



# ###  	TABLAS DE LA BASE DE DATOS 
# class EVENTOSForm(ModelForm):
# 	class Meta:
# 		model = ESTADO




