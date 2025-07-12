from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Product(models.Model):
    """
    Modelo para productos en el sistema SIP
    """
    CATEGORIA_CHOICES = [
        ('combustible', 'Combustible'),
        ('lubricante', 'Lubricante'),
        ('aditivo', 'Aditivo'),
        ('servicio', 'Servicio'),
        ('otro', 'Otro'),
    ]

    # Información básica
    name = models.CharField(max_length=255, verbose_name="Nombre del producto")
    codigo_producto = models.CharField(max_length=50, unique=True, verbose_name="Código del producto")
    description = models.TextField(verbose_name="Descripción")
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='otro', verbose_name="Categoría")
    
    # Unidad de medida y precios
    unit_of_measure = models.CharField(max_length=50, default='litros', verbose_name="Unidad de medida")
    precio_base = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio base"
    )
    precio_venta = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio de venta"
    )

    # Inventario
    stock_minimo = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Stock mínimo"
    )
    stock_actual = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Stock actual"
    )

    # Estado y fechas
    activo = models.BooleanField(default=True, verbose_name="Producto activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    @property
    def margen_ganancia(self):
        """Calcula el margen de ganancia del producto"""
        if self.precio_base > 0:
            return ((self.precio_venta - self.precio_base) / self.precio_base) * 100
        return 0

    @property
    def necesita_restock(self):
        """Indica si el producto necesita restock"""
        return self.stock_actual <= self.stock_minimo

    def __str__(self):
        return f"{self.name} ({self.codigo_producto})"
