from django.db import models

class Quote(models.Model):
    name = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    """Mapea la tabla existente "Sale" para aprovechar datos pre-cargados."""

    id = models.IntegerField(primary_key=True, db_column="id")
    compania = models.CharField(max_length=255, db_column="Compa\u00f1ia", blank=True, null=True)
    sucursal = models.CharField(max_length=255, db_column="Sucursal", blank=True, null=True)
    codigo_cliente = models.CharField(max_length=100, db_column="Cod. Cliente", blank=True, null=True)
    cliente_vnq = models.CharField(max_length=255, db_column="Cliente VNQ", blank=True, null=True)
    suplidor = models.CharField(max_length=255, db_column="Suplidor", blank=True, null=True)
    codigo_vendedor = models.CharField(max_length=50, db_column="Cod. Vendedor", blank=True, null=True)
    vendedor = models.CharField(max_length=255, db_column="Vendedor", blank=True, null=True)
    numero_factura = models.CharField(max_length=50, db_column="N\u00ba Factura", blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, db_column="Cantidad", blank=True, null=True)
    pvp_total_ext = models.DecimalField(max_digits=12, decimal_places=2, db_column="P.V.P. Total $ Extendido", blank=True, null=True)
    tipo_de_venta = models.CharField(max_length=255, db_column="Tipo de Venta", blank=True, null=True)
    cod_vend_ov = models.CharField(max_length=50, db_column="Cod.Vend.OV", blank=True, null=True)
    nombre_vendedor_ov = models.CharField(max_length=255, db_column="Nombre Vendedor OV", blank=True, null=True)
    numero_pieza = models.CharField(max_length=50, db_column="N\u00ba Pieza", blank=True, null=True)
    created_at = models.DateTimeField(db_column="createdAt")
    fecha_factura = models.CharField(max_length=255, db_column="Fecha Factura", blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"Sale"'

    def __str__(self):
        return self.numero_factura or str(self.id)
