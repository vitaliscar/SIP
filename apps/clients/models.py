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
    # Datos generales
    sucursal = models.ForeignKey('clients.Sucursal', on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField('Razón Social', max_length=255)
    codigo_cliente = models.CharField('Código Cliente', max_length=20)
    rif = models.CharField('RIF', max_length=20, blank=True, null=True)
    tipo_cliente = models.CharField('Tipo de Cliente', max_length=50, blank=True, null=True)
    estatus = models.CharField('Estatus', max_length=30, blank=True, null=True)
    fecha_registro = models.DateField('Fecha de Registro', blank=True, null=True)

    # Datos comerciales
    asesor = models.ForeignKey('users.CustomUser', null=True, blank=True, on_delete=models.SET_NULL, related_name='clientes')
    codigo_asesor = models.CharField('Código Asesor', max_length=10, blank=True, null=True)
    asesor_nombre = models.CharField('Nombre Asesor', max_length=100, blank=True, null=True)
    canal_venta = models.CharField('Canal de Venta', max_length=50, blank=True, null=True)
    segmento = models.CharField('Segmento', max_length=50, blank=True, null=True)
    grupo = models.CharField('Grupo', max_length=50, blank=True, null=True)
    subgrupo = models.CharField('Subgrupo', max_length=50, blank=True, null=True)
    clasificacion = models.CharField('Clasificación', max_length=50, blank=True, null=True)
    frecuencia_visita = models.CharField('Frecuencia de Visita', max_length=30, blank=True, null=True)
    ruta = models.CharField('Ruta', max_length=50, blank=True, null=True)

    # Datos fiscales
    contribuyente_iva = models.BooleanField('Contribuyente IVA', default=False)
    agente_retencion = models.BooleanField('Agente de Retención', default=False)
    contribuyente_especial = models.BooleanField('Contribuyente Especial', default=False)
    tipo_contribuyente = models.CharField('Tipo de Contribuyente', max_length=50, blank=True, null=True)

    # Contacto principal
    nombre_contacto = models.CharField('Nombre Contacto', max_length=100, blank=True, null=True)
    telefono_contacto = models.CharField('Teléfono Contacto', max_length=30, blank=True, null=True)
    email_contacto = models.EmailField('Email Contacto', max_length=100, blank=True, null=True)

    # Ubicación
    estado = models.CharField('Estado', max_length=50, blank=True, null=True)
    ciudad = models.CharField('Ciudad', max_length=50, blank=True, null=True)
    municipio = models.CharField('Municipio', max_length=50, blank=True, null=True)
    parroquia = models.CharField('Parroquia', max_length=50, blank=True, null=True)
    direccion = models.TextField('Dirección', blank=True, null=True)
    zona_postal = models.CharField('Zona Postal', max_length=10, blank=True, null=True)
    latitud = models.DecimalField('Latitud', max_digits=10, decimal_places=7, blank=True, null=True)
    longitud = models.DecimalField('Longitud', max_digits=10, decimal_places=7, blank=True, null=True)

    # Otros
    observaciones = models.TextField('Observaciones', blank=True, null=True)

class PotencialDeCompra(models.Model):
    cliente = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='potenciales')
    producto = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='potenciales')
    unidad_empaque = models.CharField('Unidad de Empaque', max_length=20, null=True, blank=True)
    litros_empaque = models.DecimalField('Litros por Empaque', max_digits=8, decimal_places=2, null=True, blank=True)
    potencial = models.DecimalField('Potencial de compra (litros)', max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('cliente', 'producto', 'unidad_empaque', 'litros_empaque')
        verbose_name = 'Potencial de compra'
        verbose_name_plural = 'Potenciales de compra'

    def clean(self):
        # Validación cruzada: si hay asesor y código_asesor, deben coincidir
        if self.asesor and self.codigo_asesor:
            if self.asesor.codigo_asesor != self.codigo_asesor:
                raise ValidationError('El código de asesor no coincide con el usuario asignado.')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.producto.name} ({self.potencial} L)"
