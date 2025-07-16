from django.db import models


class Product(models.Model):
    cod_chronus = models.CharField(max_length=50, blank=True, null=True)
    cod_ccv = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField('Descripción', max_length=255)
    calidad_categoria = models.CharField(max_length=100, blank=True, null=True)
    uso = models.CharField(max_length=255, blank=True, null=True)
    unidad_empaque = models.CharField(max_length=50, blank=True, null=True)
    litros_unidad = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    lts = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unidades_x_ue = models.IntegerField(blank=True, null=True)
    venta_detalle = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name
