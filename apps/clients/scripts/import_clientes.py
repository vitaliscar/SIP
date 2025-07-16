import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()
from apps.clients.models import Sucursal, Client
from apps.users.models import CustomUser

import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()
from apps.clients.models import Sucursal, Client
from apps.users.models import CustomUser

def run():
    csv_file_path = r'd:\Users\v52anap\Documents\sales_intelligence_platform\Datos\Ficha Maestra CCV - Listado de clientes (4).csv'
    with open(csv_file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sucursal_nombre = row['Sucursal'].strip() if row['Sucursal'] else None
            cliente_nombre = row['Cliente'].strip() if row['Cliente'] else None
            codigo_cliente = row['Codigo Cliente'].strip() if row['Codigo Cliente'] else None
            asesor_nombre = row['Asesor'].strip() if 'Asesor' in row and row['Asesor'] else None
            codigo_asesor = row['Codigo Asesor'].strip() if 'Codigo Asesor' in row and row['Codigo Asesor'] else None
            if not cliente_nombre or not codigo_cliente:
                continue
            sucursal, _ = Sucursal.objects.get_or_create(nombre=sucursal_nombre) if sucursal_nombre else (None, False)
            # Guardar nombre y código de asesor
            client, created = Client.objects.get_or_create(
                codigo_cliente=codigo_cliente,
                sucursal=sucursal,
                defaults={'nombre': cliente_nombre, 'asesor': None, 'codigo_asesor': codigo_asesor, 'asesor_nombre': asesor_nombre}
            )
            if not created:
                client.nombre = cliente_nombre
                client.asesor = None
                client.codigo_asesor = codigo_asesor
                client.asesor_nombre = asesor_nombre
                client.save()
            print(f"Cliente registrado: {cliente_nombre} | Sucursal: {sucursal_nombre} | Código asesor: {codigo_asesor} | Nombre asesor: {asesor_nombre}")
