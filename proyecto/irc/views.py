from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.context import RequestContext
from .forms import FormularioCrearForm, FormularioPararForm, FormularioRegistroForm, SignUpForm, FormularioEstadoForm
from .models import FormularioCrear, FormularioParar, FormularioRegistro, FormularioEstado
from xmlrpclib      import * 
from django.contrib import admin
from django.db import connections
import os
import sqlite3

##########################################################################################
##################################### CONEXION ###########################################
##########################################################################################
puertoIRC   =  9000
rpc         = ServerProxy('http://localhost:9000', allow_none=True)
# Cliente = Cliente()
print "Conectando al puerto %s...\n" %(puertoIRC)


##########################################################################################
##################################### FUNCIONES ##########################################
##########################################################################################
@login_required()
def inicio(request):
    titulo  = "INICIO"
    form    = FormularioRegistroForm(request.POST or None)
    context = {
    "titulo": titulo,
    "form"  : form,
    }

    if form.is_valid():
        instance    = form.save(commit = False)
        usuario     = form.cleaned_data.get("nombre")
        email       = form.cleaned_data.get("email")
        form.save()

        context = {
        "titulo": "Gracias %s! Estas registrado." %(usuario),
        "form"  : form,
        }

        if not usuario: 
            context = {
            "titulo": "Gracias %s! Estas registrado." %(email),
            "form": form,
            "user": request.user
            }
    return render(request,"inicio.html", context)

@login_required()
def crear(request):
    titulo  = "Lanza tu BOT"
    form    = FormularioCrearForm(request.POST or None) 
    context = {
    "titulo": titulo,
    "form"  : form,
    }
    
    if form.is_valid():
        instance    = form.save(commit = False)
        nombre      = form.cleaned_data.get("nombre")
        servidor    = form.cleaned_data.get("servidor")
        canal       = form.cleaned_data.get("canal")
        canal       = "#" + canal
        puerto      = form.cleaned_data.get("puerto")
        patron      = form.cleaned_data.get("patron")
        form.save()
        crear       = rpc.crear(servidor, canal, nombre, puerto, patron)
        context     = {
        "titulo": "Bot Creado",
        "form"  : form,
        }

    return render(request,"crear.html", context)
 
@login_required()
def parar(request):
    titulo  = "Para tu BOT"
    form    = FormularioPararForm(request.POST or None) 
    context = {
    "titulo": titulo,
    "form"  : form,
    }


    if form.is_valid():
        instance    = form.save(commit = False)
        ID_BOT      = form.cleaned_data.get("ID_BOT")
        form.save()
        parar       = rpc.desconexion(ID_BOT)

        context     = {
        "titulo": "El bot se ha parado",
        "form"  : form,
        }

    return render(request,"parar.html", context)


##########################################################################################
################################# CONSULTA A LA DB #######################################
##########################################################################################

@login_required()
def bot_info(request):
    titulo  = "Consulta el estado del Bot"
    form    = FormularioEstadoForm(request.POST or None) 
    context = {
    "titulo": titulo,
    "form"  : form,
    }
       

    if form.is_valid():
        instance    = form.save(commit = False)
        ID_BOT      = form.cleaned_data.get("ID_BOT")
        form.save()

        con        = sqlite3.connect('C:/DjangoProyectos/irc.db')  #con_bd.close()
        cursor     = con.cursor()  #cursor.close()
        reintentar = False
        print " OK!  DB Abierta."
        cursor.execute("SELECT * FROM BOT_INFO WHERE  ID_BOT == '%s'" %(ID_BOT))
        estado = cursor.fetchall()
  
        aux = []   # lista_datos_bot
        aux1 = []
        for i in estado:
            aux = list(i)
            aux1.append(aux)
        # print aux1

        titulillos = ["ID Conversacion", "ID Bot", "Inicio", "Ultima Actualizacion", "Servidor", "Canal", "Numero de Eventos", "Numero de Mensajes Capturados", "Estado"]
        datos = []
        for i in aux1:
            for index, k in enumerate(i):
                datos.append(k)
  
        con.close()
        context = {
        "titulo"    : "Consulta el estado del BOT",
        "form"      : form,
        "estado"    : estado,
        "titulillos": titulillos,
        "AUX"       : aux1,
        "DATOS"     : datos,
        }
    else:
        context = {
        "titulo": titulo,
        "form"  : form,
        }

    return render(request,"bot_info.html", context)

@login_required()
def mensajes(request):
    titulo  = "Visualizacion de los mensajes capturados por los BOT"
    form    = FormularioEstadoForm(request.POST or None) 
    context = {
    "titulo": titulo,
    "form"  : form,
    }

    if form.is_valid():
        instance   = form.save(commit = False)
        ID_BOT     = form.cleaned_data.get("ID_BOT")
        form.save()

        con        = sqlite3.connect('C:/DjangoProyectos/irc.db')  #con_bd.close()
        cursor     = con.cursor()  #cursor.close()
        reintentar = False
        print " OK!  DB Abierta."        
        ID_BOT = ID_BOT + "%"
        cursor.execute("SELECT * FROM MENSAJES WHERE ID_MSG LIKE '%s' "%(ID_BOT))
        estado = cursor.fetchall()

        aux = []   # lista_datos_bot
        aux1 = []
        for i in estado:
            aux = list(i)
            aux1.append(aux)
        # print aux1

        titulillos = ["ID Mensaje", "Fecha", "Canal", "Servidor", "Usuario", "Mensaje"]
        datos = []
        for i in aux1:
            for index, k in enumerate(i):
                datos.append(k)
  
        con.close()
        context = {
        "titulo"    : "Consulta el estado del BOT",
        "form"      : form,
        "estado"    : estado,
        "titulillos": titulillos,
        "AUX"       : aux1,
        "DATOS"     : datos,
        }

    else:
        context = {
        "titulo"    : titulo,
        "form"      : form,
        }

    # Pasamos al template el diccionario como si fuera un queryset normal
    return render(request,"mensajes.html", context)

@login_required()
def eventos(request):
    titulo  = "Visualizacion de los mensajes capturados por los BOT"
    form    = FormularioEstadoForm(request.POST or None) 
    context = {
    "titulo": titulo,
    "form"  : form,
    }

    if form.is_valid():
        instance   = form.save(commit = False)
        ID_BOT   = form.cleaned_data.get("ID_BOT")
        form.save()
        con        = sqlite3.connect('C:/DjangoProyectos/irc.db')  #con_bd.close()
        cursor     = con.cursor()  #cursor.close()
        reintentar = False
        print " OK!  DB Abierta."
        ID_BOT = ID_BOT + "%"
        cursor.execute("SELECT * FROM EVENTO WHERE ID_EVENT LIKE '%s' "%(ID_BOT))
        estado = cursor.fetchall()

        aux = []   # lista_datos_bot
        aux1 = []
        for i in estado:
            aux = list(i)
            aux1.append(aux)
        # print aux1

        titulillos = ["ID Evento", "Fecha", "Canal", "Servidor", "Patron"]
        datos = []
        for i in aux1:
            for index, k in enumerate(i):
                datos.append(k)
  
        con.close()
        context = {
        "titulo"    : "Consulta el estado del BOT",
        "form"      : form,
        "estado"    : estado,
        "titulillos": titulillos,
        "AUX"       : aux1,
        "DATOS"     : datos,
        }

    else:
        context = {
        "titulo"    : titulo,
        "form"      : form,
        }

    # Pasamos al template el diccionario como si fuera un queryset normal
    return render(request,"eventos.html", context)




##########################################################################################
##################################### REGISTRO ###########################################
##########################################################################################

#   Dicha vista se ocupara unicamente de redirigir a la plantilla de la pagina de inicio:
def main(request):
    titulo  = "MENU DE INICIO" 
    context = {
    "titulo": titulo,
    }
    return render(request,'main.html', context)

 # se ocupara de recoger la informacion introducida por el usuario a traves del formulario y 
 # de darlo de alta en el sistema. Si se produce alguna excepcion al dar de alta el usuario, 
 # como por ejemplo que el nombre del usuario ya exista en la base de datos o que la direccion 
 # de correo introducida sea incorrecta, el usuario sera informado:
def signup(request):
    titulo = "REGISTRO"

    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass 
            # Process the data in form.cleaned_data
            username    = form.cleaned_data["username"]
            password    = form.cleaned_data["password"]
            email       = form.cleaned_data["email"]
            first_name  = form.cleaned_data["first_name"]
            last_name   = form.cleaned_data["last_name"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user            = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name  = last_name
 
            # Save new user attributes
            user.save() 

            return HttpResponseRedirect(reverse('login'))  # Redirect after POST
    else:
        form = SignUpForm()

    data   = {
    "titulo": titulo,    
    'form': form,
    } 
    return render(request,'signup.html',  data)


