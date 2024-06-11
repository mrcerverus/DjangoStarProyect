"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='indice'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('welcome/', welcome, name='welcome'),
    path('editar_usuario/', editar_usuario, name='editar_usuario'),
    path('password/', cambiar_contrasena, name='cambiar_contrasena'),
    path('formulario_contacto/',formulario_contacto, name='formulario_contacto'),
]

#para cargar imagenes desde base de datos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
