from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

#Index
def index(request):
    return render(request,'index.html', {})

#Welcome
def welcome(request):
    return render(request, 'welcome.html', {})

#Formulario de Contacto
def formulario_contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Su mensaje fue enviado con exito')
            return redirect('indice')
    else:
        form = ContactForm()
    return render(request, 'registration/contacto.html', {'form': form})

#Formulario de registro
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            usuario = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, usuario)
            return redirect('indice')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

#Actualizar Usuario
@login_required
def editar_usuario(request):
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = UsuarioEditForm(instance=request.user)

    return render(request, 'registration/editar_usuario.html', {'form': form})

#Actualizar Contrasena
@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantener al usuario autenticado después de cambiar la contraseña
            messages.success(request, '¡Tu contraseña ha sido cambiada exitosamente!')
            return redirect('welcome')  # Redirige a una página de perfil u otra página relevante
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'registration/cambiar_contrasena.html', {'form': form})