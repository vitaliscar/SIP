from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Report(models.Model):
    """
    Modelo para reportes generados en el sistema SIP
    """
    REPORT_TYPES = [
        ('ventas', 'Reporte de Ventas'),
        ('clientes', 'Reporte de Clientes'),
        ('productos', 'Reporte de Productos'),
        ('sucursales', 'Reporte de Sucursales'),
        ('metas', 'Reporte de Metas'),
        ('ai_forecast', 'Reporte de Pronósticos IA'),
        ('custom', 'Reporte Personalizado'),
    ]

    nombre = models.CharField(max_length=255, verbose_name="Nombre del reporte")
    tipo = models.CharField(max_length=20, choices=REPORT_TYPES, verbose_name="Tipo de reporte")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    parametros = models.JSONField(default=dict, blank=True, verbose_name="Parámetros del reporte")
    datos = models.JSONField(default=dict, blank=True, verbose_name="Datos del reporte")
    archivo = models.FileField(upload_to='reportes/', blank=True, null=True, verbose_name="Archivo del reporte")
    
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportes_creados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_generacion = models.DateTimeField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"