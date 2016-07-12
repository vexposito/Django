from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import FormularioCrear, FormularioParar, FormularioRegistro, FormularioEstado
 
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

# class FormularioInicialForm(forms.Form):

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
