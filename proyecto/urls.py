"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns
from django.contrib import admin
from django.contrib.auth.views import login, logout # Para usar la vista que nos proporciona Django

from irc import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main, name = 'main'),
    url(r'^inicio/$', views.inicio, name = 'inicio'),
    url(r'^crear/$', views.crear, name = 'crear'),
    url(r'^parar/$', views.parar, name = 'parar'),
    url(r'^estado/$', views.estado, name = 'estado'),
    url(r'^msg_db/$', views.msg_db, name = 'msg_db'),   
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(r'^login/$', login, {'template_name': 'login.html', }, name="login"),
]
