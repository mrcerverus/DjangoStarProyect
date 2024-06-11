from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from itertools import cycle
from django.core.exceptions import ValidationError
import re

#Validacion Rut:
def validate_rut(value):
    # Expresión regular para el formato del RUT
    rut_regex = re.compile(r'^\d{1,2}\d{3}\d{3}-[\dkK]$')
    if not rut_regex.match(value):
        raise ValidationError('El RUT debe tener el formato XXXXXXXXX-X')
    
    # Separar el número del dígito verificador
    rut_body, dv = value.split('-')
    rut_body = int(rut_body)
    
    # Calcular el dígito verificador
    reversed_digits = map(int, reversed(str(rut_body)))
    factors = cycle(range(2, 8))
    checksum = sum(d * f for d, f in zip(reversed_digits, factors))
    calculated_dv = (-checksum) % 11
    if calculated_dv == 10:
        calculated_dv = 'K'
    else:
        calculated_dv = str(calculated_dv)
    
    if dv.upper() != calculated_dv:
        raise ValidationError('El RUT no es válido')

# Create your models here.

#Usuario personalizado
class Usuario(AbstractUser):
    #Propiedades personzalizadas
    TIPO_USER_CHOICES = [
        ('ARRENDADOR', 'arrendador'),
        ('ARRENDATARIO', 'arrendatario'),
    ]

    # nombre = models.CharField(max_length=50)
    # apellido = models.CharField( max_length=50)
    rut = models.CharField(max_length=12, validators=[validate_rut])
    direccion = models.CharField(max_length=50)
    telefono = PhoneNumberField(blank=False, null=False,verbose_name="Telefono de contacto")
    # correo = models.EmailField(max_length=254)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USER_CHOICES, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.rut}"



#Formulario de contacto
class ContactForm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre', null=False, blank=False)
    last_name = models.CharField(max_length=100, verbose_name='Apellidos', null=False, blank=False)
    phone = PhoneNumberField(verbose_name='Telefono de Contacto', null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(verbose_name='Mensaje')

    def __str__(self):
        return f"Mensaje de {self.name}, correo: {self.email}"