from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from decimal import Decimal


User = get_user_model()


class SalesGoal(models.Model):
    name = models.CharField(max_length=255)
    target = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Goal(models.Model):
    """
    Modelo para metas de ventas en el sistema SIP
    """
    PERIODO_CHOICES = [
        ('mensual', 'Mensual'),
        ('trimestral', 'Trimestral'),
        ('semestral', 'Semestral'),
        ('anual', 'Anual'),
    ]

    TIPO_CHOICES = [
        ('ventas', 'Meta de Ventas'),
        ('clientes', 'Meta de Clientes'),
        ('productos', 'Meta de Productos'),
        ('sucursal', 'Meta de Sucursal'),
    ]

    # Información básica
    nombre = models.CharField(max_length=255, verbose_name="Nombre de la meta")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo de meta")
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES, verbose_name="Período")

    # Valores objetivo
    valor_objetivo = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Valor objetivo"
    )
    valor_actual = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Valor actual"
    )

    # Asignaciones
    sucursal = models.ForeignKey(
        'clients.Sucursal', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        related_name='metas'
    )
    asesor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='metas_asignadas'
    )
    producto = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='metas'
    )

    # Fechas
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de fin")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    # Estado
    activa = models.BooleanField(default=True, verbose_name="Meta activa")
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='metas_creadas')

    class Meta:
        verbose_name = "Meta"
        verbose_name_plural = "Metas"
        ordering = ['-fecha_creacion']

    @property
    def porcentaje_cumplimiento(self):
        """Calcula el porcentaje de cumplimiento de la meta"""
        if self.valor_objetivo > 0:
            return (self.valor_actual / self.valor_objetivo) * 100
        return 0

    def __str__(self):
        return f"{self.nombre} ({self.get_periodo_display()})"
