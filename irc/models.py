from __future__ import unicode_literals
from django.db import models

class FormularioRegistro(models.Model):
	nombre 			= models.CharField(max_length=100, blank=False, null=False)
	apellidos 		= models.CharField(max_length=100, blank=False, null=False)
	email 			= models.EmailField()	
	codigo_postal   = models.IntegerField()
	timeStamp 		= models.DateTimeField(auto_now_add = True, auto_now = False)
	def __unicode__(self):
		return self.nombre

class FormularioCrear(models.Model):
	servidor 	= models.CharField(max_length=100, blank=False, null=False)
	puerto 		= models.IntegerField()
	canal 	    = models.CharField(max_length=100, blank=False, null=False)
	nombre	 	= models.CharField(max_length=100, blank=False, null=False)
	patron 		= models.CharField(max_length=100, blank=False, null=False)
	def __unicode__(self):
		return self.nombre

class FormularioParar(models.Model):
	ID_BOT 		= models.CharField(max_length=100, blank=False, null=False)
	def __unicode__(self):
		return self.ID_BOT

class FormularioEstado(models.Model):
	ID_BOT 		= models.CharField(max_length=100, blank=False, null=False)
	def __unicode__(self):
		return self.ID_BOT

####	MODELOS DE LA BASE DE DATOS CREADA POR EL MASTER: MENSAJE, EVENTOS, BOT_INFO


