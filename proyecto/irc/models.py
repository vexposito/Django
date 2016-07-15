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
class EVENTOS(models.Model):
	ID_EVENT 	= models.CharField(max_length=100, blank=False, null=False)
	FECHA 		= models.IntegerField()
	CANAL  		= models.CharField(max_length=100, blank=False, null=False)
	SERVIDOR 	= models.CharField(max_length=100, blank=False, null=False)
	PATRON 		= models.CharField(max_length=100, blank=False, null=False)
	def __unicode__(self):
		return self.ID_EVENT

class MENSAJES(models.Model):
	ID_MSG		= models.CharField(max_length=100, blank=False, null=False)
	FECHA  		= models.IntegerField()
	CANAL 		= models.CharField(max_length=100, blank=False, null=False)
	SERVIDOR 	= models.CharField(max_length=100, blank=False, null=False)
	USUARIO 	= models.CharField(max_length=100, blank=False, null=False)
	MENSAJE 	= models.CharField(max_length=1000, blank=False, null=False)	
	def __unicode__(self):
		return self.ID_MSG

class BOT_INFO(models.Model):
	ID_CONVERS  = models.CharField(max_length=100, blank=False, null=False)
	ID_BOT 		= models.CharField(max_length=100, blank=False, null=False)
	INICIO 		= models.IntegerField()
	ULTIMA		= models.IntegerField()
	SERVIDOR 	= models.CharField(max_length=100, blank=False, null=False)
	CANAL 		= models.CharField(max_length=100, blank=False, null=False)
	EVENTOS     = models.IntegerField()
	NUM_MSG		= models.IntegerField()
	ESTADO  	= models.CharField(max_length=100, blank=False, null=False)
	def __unicode__(self):
		return self.ID_CONVERS

