import csv
from apps.clients.models import Client, PotencialDeCompra
from apps.products.models import Product

def run():
    csv_file_path = r'D:\Users\v52anap\Documents\sales_intelligence_platform\Datos\Ficha Maestra CCV - Potencial (4).csv'
    litros_col = 'Litros Potenciales'
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        print(f"Columnas detectadas: {reader.fieldnames}")
        for row in reader:
            try:
                import unicodedata
                def limpiar_texto(texto):
                    if not texto:
                        return ''
                    texto = unicodedata.normalize('NFKD', texto)
                    texto = texto.encode('ascii', 'ignore').decode('ascii')
                    # Eliminar símbolos especiales excepto letras, números y espacios
                    import re
                    texto = re.sub(r'[^A-Za-z0-9 ]+', '', texto)
                    return texto.upper().strip()

                sucursal = limpiar_texto(row['Sucursal'])
                asesor = limpiar_texto(row['Asesor'])
                codigo_asesor = limpiar_texto(row['Codigo Asesor'])
                cliente = limpiar_texto(row['Cliente'])
                codigo_cliente = limpiar_texto(row['Codigo Cliente'])
                # Normalización: eliminar ceros a la izquierda y espacios
                if codigo_cliente:
                    codigo_cliente = codigo_cliente.lstrip('0').replace(' ', '')
                producto_nombre = limpiar_texto(row['Producto'])
                unidad_empaque = limpiar_texto(row.get('U.E.', ''))
                litros_empaque_raw = row.get('Litros Empaque', '').strip()
                litros_empaque_raw = litros_empaque_raw.replace('.', '').replace(',', '.')
                try:
                    litros_empaque = float(litros_empaque_raw) if litros_empaque_raw else None
                except ValueError:
                    print(f"Error convirtiendo litros empaque: '{row.get('Litros Empaque', '')}' → '{litros_empaque_raw}'")
                    litros_empaque = None
                # Conversión correcta de miles y decimales para Venezuela
                litros_raw = row[litros_col].strip()
                # Primero elimina puntos (separador de miles), luego cambia coma por punto (decimal)
                litros_raw = litros_raw.replace('.', '').replace(',', '.')
                try:
                    litros = float(litros_raw) if litros_raw else 0.0
                except ValueError:
                    print(f"Error convirtiendo litros: '{row[litros_col]}' → '{litros_raw}'")
                    litros = 0.0
            except Exception as e:
                print(f"Error en fila: {row}\n{e}")
                continue

            # Buscar el cliente por código, sucursal y asesor
            print(f"Buscando cliente: sucursal='{sucursal}', codigo_cliente='{codigo_cliente}', codigo_asesor='{codigo_asesor}'")
            cliente_obj = get_cliente(codigo_cliente, sucursal, codigo_asesor)
            if not cliente_obj and codigo_asesor:
                # Si no se encuentra con asesor, intentar solo con código y sucursal
                print(f"Intentando búsqueda sin asesor...")
                cliente_obj = get_cliente(codigo_cliente, sucursal, None)
            if not cliente_obj:
                print(f"Cliente no encontrado: {{'sucursal': sucursal, 'codigo_cliente': codigo_cliente, 'codigo_asesor': codigo_asesor}}")
                # Mostrar ejemplos de clientes en la base para comparar
                from apps.clients.models import Client
                ejemplos = Client.objects.all()[:5]
                print("Ejemplos de clientes en la base:")
                for ej in ejemplos:
                    print(f"codigo_cliente='{ej.codigo_cliente}', sucursal='{ej.sucursal.nombre}', codigo_asesor='{getattr(ej, 'codigo_asesor', '')}'")
                continue


            # Buscar el producto por nombre (puede haber duplicados)
            from apps.products.models import Product
            productos_qs = Product.objects.filter(name__iexact=producto_nombre)
            if productos_qs.count() == 0:
                # Si no existe, crearlo
                producto_obj = Product.objects.create(name=producto_nombre)
                print(f"Producto creado automáticamente: {producto_nombre}")
            elif productos_qs.count() == 1:
                producto_obj = productos_qs.first()
            else:
                producto_obj = productos_qs.first()
                print(f"ADVERTENCIA: Hay {productos_qs.count()} productos con el nombre '{producto_nombre}'. Se usará el primero con id={producto_obj.id}")

            if litros > 0 and unidad_empaque and litros_empaque is not None:
                from decimal import Decimal
                litros_decimal = Decimal(str(litros))
                litros_empaque_decimal = Decimal(str(litros_empaque))
                pot, created = PotencialDeCompra.objects.get_or_create(
                    cliente=cliente_obj,
                    producto=producto_obj,
                    unidad_empaque=unidad_empaque,
                    litros_empaque=litros_empaque_decimal,
                    defaults={'potencial': litros_decimal}
                )
                if not created:
                    pot.potencial += litros_decimal
                    pot.save()
                print(f"Potencial registrado: Cliente={cliente_obj}, Producto={producto_obj}, U.E.={unidad_empaque}, Litros Empaque={litros_empaque_decimal}, Litros acumulados={pot.potencial}")
            else:
                print(f"Potencial ignorado (<=0 o datos incompletos): Cliente={cliente_obj}, Producto={producto_obj}, U.E.={unidad_empaque}, Litros Empaque={litros_empaque}, Litros={litros}")

def get_cliente(codigo_cliente, sucursal_nombre, codigo_asesor):
    from apps.clients.models import Sucursal
    import unicodedata
    import re
    def limpiar_texto(texto):
        if not texto:
            return ''
        texto = unicodedata.normalize('NFKD', texto)
        texto = texto.encode('ascii', 'ignore').decode('ascii')
        texto = re.sub(r'[^A-Za-z0-9 ]+', '', texto)
        return texto.upper().strip()

    sucursal_nombre = limpiar_texto(sucursal_nombre)
    codigo_cliente = limpiar_texto(str(codigo_cliente))
    codigo_asesor = limpiar_texto(str(codigo_asesor)) if codigo_asesor else ''
    print(f"get_cliente: sucursal_nombre='{sucursal_nombre}', codigo_cliente='{codigo_cliente}', codigo_asesor='{codigo_asesor}'")
    try:
        sucursal = Sucursal.objects.get(nombre__iexact=sucursal_nombre)
    except Sucursal.DoesNotExist:
        print(f"Sucursal no encontrada: '{sucursal_nombre}'")
        return None
    # Normalización: eliminar ceros a la izquierda y espacios
    codigo_cliente = codigo_cliente.lstrip('0').replace(' ', '')
    filtros = {
        'codigo_cliente': codigo_cliente,
        'sucursal': sucursal
    }
    if codigo_asesor:
        filtros['codigo_asesor'] = codigo_asesor
    print(f"Filtros usados en Client.objects.filter: {filtros}")
    clientes = Client.objects.filter(**filtros)
    print(f"Clientes encontrados: {clientes.count()}")
    if clientes.exists():
        print(f"Cliente encontrado: codigo_cliente='{codigo_cliente}', sucursal='{sucursal.nombre}', codigo_asesor='{codigo_asesor}'")
        return clientes.first()
    return None

def get_producto(nombre_producto):
    try:
        return Product.objects.get(name=nombre_producto.strip())
    except Product.DoesNotExist:
        return None

