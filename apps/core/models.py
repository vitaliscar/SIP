from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Configuracion(models.Model):
    """
    Modelo para configuraciones generales del sistema SIP
    """
    clave = models.CharField(max_length=100, unique=True, verbose_name="Clave de configuración")
    valor = models.TextField(verbose_name="Valor")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    activa = models.BooleanField(default=True, verbose_name="Configuración activa")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuraciones"
        ordering = ['clave']

    def __str__(self):
        return f"{self.clave}: {self.valor[:50]}..."