from django.db import models
from django.core.exceptions import ValidationError

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

SUCURSALES_PREDEFINIDAS = [
    'Puerto Ordaz',
    'Puerto la Cruz',
    'Barquisimeto',
    'Valencia',
    'Caracas',
    'Maracaibo',
]

class Client(models.Model):
    sucursal = models.ForeignKey('clients.Sucursal', on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(max_length=255)
    codigo_cliente = models.CharField(max_length=20, unique=True)
    asesor = models.ForeignKey('users.CustomUser', null=True, blank=True, on_delete=models.SET_NULL, related_name='clientes')
    codigo_asesor = models.CharField(max_length=10, blank=True, null=True)
    potential_purchase = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def clean(self):
        # Validación cruzada: si hay asesor y código_asesor, deben coincidir
        if self.asesor and self.codigo_asesor:
            if self.asesor.codigo_asesor != self.codigo_asesor:
                raise ValidationError('El código de asesor no coincide con el usuario asignado.')

    def save(self, *args, **kwargs):
        # Normaliza el nombre capitalizándolo
        if self.nombre:
            self.nombre = self.nombre.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
