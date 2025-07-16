import os
import django
import csv
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()
from apps.products.models import Product

def run():
    csv_file_path = r'd:\Users\v52anap\Documents\sales_intelligence_platform\Datos\Ficha Maestra CCV - Productos (1).csv'
    # Borrar todos los productos antes de importar
    Product.objects.all().delete()
    print('Todos los productos eliminados. Importando desde cero...')
    with open(csv_file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        print(f"Columnas detectadas: {reader.fieldnames}")
        for row in reader:
            nombre = row.get('Descripción') or row.get('DescripciÃ³n') or row.get('Descripcion') or row.get('Producto') or row.get('Nombre')
            if not nombre:
                nombre = 'SIN NOMBRE'
            nombre = nombre.strip()
            def parse_decimal(val):
                try:
                    return float(val.replace(',', '.'))
                except (ValueError, AttributeError):
                    return None

            def parse_int(val):
                try:
                    return int(val)
                except (ValueError, TypeError):
                    return None

            unidad_empaque = row.get('Unidad Empaque', '').strip() or None
            unidades_x_ue_val = row.get('Unidades x U.E', '').strip()
            unidades_x_ue = parse_int(unidades_x_ue_val)
            if unidades_x_ue is None and unidades_x_ue_val:
                if unidad_empaque:
                    unidad_empaque = f"{unidad_empaque} | {unidades_x_ue_val}"
                else:
                    unidad_empaque = unidades_x_ue_val

            # Crear un producto por cada fila, sin deduplicar por nombre ni códigos
            product = Product(
                name=nombre,
                cod_chronus=row.get('Cod. Chronus', '').strip() or None,
                cod_ccv=row.get('Cod. CCV', '').strip() or None,
                calidad_categoria=row.get('Calidad / Categoria', '').strip() or None,
                uso=row.get('USO', '').strip() or None,
                unidad_empaque=unidad_empaque,
                litros_unidad=parse_decimal(row.get('Litros Unidad', '')),
                lts=parse_decimal(row.get('LTS', '')),
                unidades_x_ue=unidades_x_ue,
                venta_detalle=row.get('Venta Detalle', '').strip() or None,
            )
            product.save()
            print(f"Producto registrado: {nombre} | Cod. Chronus: {product.cod_chronus} | Cod. CCV: {product.cod_ccv}")

run()
