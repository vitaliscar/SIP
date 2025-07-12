from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class AIModelConfig(models.Model):
    name = models.CharField(max_length=255)
    configuration = models.JSONField()

    def __str__(self):
        return self.name


class ForecastResult(models.Model):
    """
    Modelo para almacenar resultados de pronósticos de IA
    """
    TIPO_FORECAST_CHOICES = [
        ('ventas', 'Pronóstico de Ventas'),
        ('demanda', 'Pronóstico de Demanda'),
        ('clientes', 'Pronóstico de Clientes'),
        ('productos', 'Pronóstico de Productos'),
        ('sucursal', 'Pronóstico de Sucursal'),
    ]

    ESTADO_CHOICES = [
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('error', 'Error'),
    ]

    # Información básica
    nombre = models.CharField(max_length=255, verbose_name="Nombre del pronóstico")
    tipo = models.CharField(max_length=20, choices=TIPO_FORECAST_CHOICES, verbose_name="Tipo de pronóstico")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    # Configuración del modelo de IA
    modelo_ia = models.ForeignKey(
        AIModelConfig,
        on_delete=models.CASCADE,
        related_name='forecast_results',
        verbose_name="Modelo de IA utilizado"
    )
    parametros_entrada = models.JSONField(default=dict, verbose_name="Parámetros de entrada")
    
    # Resultados del pronóstico
    resultado = models.JSONField(default=dict, verbose_name="Resultado del pronóstico")
    confianza = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        blank=True, 
        null=True,
        verbose_name="Nivel de confianza (%)"
    )
    precision = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        blank=True, 
        null=True,
        verbose_name="Precisión del modelo (%)"
    )

    # Período del pronóstico
    fecha_inicio_forecast = models.DateField(verbose_name="Fecha inicio del pronóstico")
    fecha_fin_forecast = models.DateField(verbose_name="Fecha fin del pronóstico")

    # Asignaciones opcionales
    sucursal = models.ForeignKey(
        'clients.Sucursal',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='forecasts'
    )
    producto = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='forecasts'
    )
    asesor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='forecasts'
    )

    # Control de ejecución
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='procesando')
    mensaje_error = models.TextField(blank=True, null=True, verbose_name="Mensaje de error")
    
    # Auditoría
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forecasts_creados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_procesamiento = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Resultado de Pronóstico"
        verbose_name_plural = "Resultados de Pronósticos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} - {self.get_tipo_display()} ({self.estado})"
