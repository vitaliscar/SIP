from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from decimal import Decimal


User = get_user_model()


class Quote(models.Model):
    name = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    """
    Modelo para registrar las ventas realizadas en el sistema SIP
    """
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('entregada', 'Entregada'),
        ('facturada', 'Facturada'),
        ('cancelada', 'Cancelada'),
    ]

    # Información básica de la venta
    codigo_venta = models.CharField(max_length=50, unique=True, verbose_name="Código de venta")
    cliente = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='ventas')
    producto = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='ventas')
    sucursal = models.ForeignKey('clients.Sucursal', on_delete=models.CASCADE, related_name='ventas')
    asesor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas_realizadas')

    # Detalles de la venta
    cantidad = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Cantidad"
    )
    precio_unitario = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio unitario"
    )
    total = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Total"
    )
    descuento = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(Decimal('0')), MinValueValidator(Decimal('100'))],
        verbose_name="Descuento (%)"
    )

    # Estado y fechas
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_venta = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    # Observaciones
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta']

    def save(self, *args, **kwargs):
        # Calcular el total automáticamente
        if self.cantidad and self.precio_unitario:
            subtotal = self.cantidad * self.precio_unitario
            descuento_amount = subtotal * (self.descuento / 100)
            self.total = subtotal - descuento_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo_venta} - {self.cliente.nombre} - ${self.total}"
