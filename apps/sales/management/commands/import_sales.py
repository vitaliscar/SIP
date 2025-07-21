import csv
from django.core.management.base import BaseCommand
from apps.sales.models import Sale

class Command(BaseCommand):
    help = 'Importa ventas desde un archivo CSV existente.'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Ruta del archivo CSV a importar')

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sale, created = Sale.objects.get_or_create(
                    numero_factura=row.get('N\u00ba Factura'),
                    defaults={
                        'compania': row.get('Compa\u00f1ia'),
                        'sucursal': row.get('Sucursal'),
                        'codigo_cliente': row.get('Cod. Cliente'),
                        'cliente_vnq': row.get('Cliente VNQ'),
                        'suplidor': row.get('Suplidor'),
                        'codigo_vendedor': row.get('Cod. Vendedor'),
                        'vendedor': row.get('Vendedor'),
                        'cantidad': row.get('Cantidad') or 0,
                        'pvp_total_ext': row.get('P.V.P. Total $ Extendido') or 0,
                        'tipo_de_venta': row.get('Tipo de Venta'),
                        'cod_vend_ov': row.get('Cod.Vend.OV'),
                        'nombre_vendedor_ov': row.get('Nombre Vendedor OV'),
                        'numero_pieza': row.get('N\u00ba Pieza'),
                        'created_at': row.get('createdAt') or row.get('created_at'),
                        'fecha_factura': row.get('Fecha Factura'),
                    }
                )
                if not created:
                    for field, key in [
                        ('compania', 'Compa\u00f1ia'),
                        ('sucursal', 'Sucursal'),
                        ('codigo_cliente', 'Cod. Cliente'),
                        ('cliente_vnq', 'Cliente VNQ'),
                        ('suplidor', 'Suplidor'),
                        ('codigo_vendedor', 'Cod. Vendedor'),
                        ('vendedor', 'Vendedor'),
                        ('cantidad', 'Cantidad'),
                        ('pvp_total_ext', 'P.V.P. Total $ Extendido'),
                        ('tipo_de_venta', 'Tipo de Venta'),
                        ('cod_vend_ov', 'Cod.Vend.OV'),
                        ('nombre_vendedor_ov', 'Nombre Vendedor OV'),
                        ('numero_pieza', 'N\u00ba Pieza'),
                        ('created_at', 'createdAt'),
                        ('fecha_factura', 'Fecha Factura'),
                    ]:
                        setattr(sale, field, row.get(key))
                    sale.save()
                self.stdout.write(self.style.SUCCESS(f"Procesada factura {sale.numero_factura}"))
        self.stdout.write(self.style.SUCCESS('Importaci\u00f3n finalizada.'))
