from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


#Formulario Creacion de Usuario
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'password1',
            'password2',
            'rut',
            'first_name',
            'last_name',
            'direccion',
            'email',
            'telefono',
            'tipo_usuario'
            ]
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))


#Formulario edicion de usuario
class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'direccion', 'telefono', 'email']

    def __init__(self, *args, **kwargs):
        super(UsuarioEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios'))
        if 'password' in self.fields:
            del self.fields['password']

#Formulario cambio de password
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Cambiar Contraseña'))


#Formulario de contacto
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'name',
            'last_name',
            'phone', 
            'email',
            'message'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))