import csv
import os
import django
import sys

# Configura el entorno Django
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.clients.models import Client, Sucursal
from apps.users.models import CustomUser

CSV_PATH = r'd:\Users\v52anap\Downloads\Ficha Maestra CCV - Listado de clientes (2).csv'

def get_or_create_sucursal(nombre):
    sucursal, _ = Sucursal.objects.get_or_create(nombre=nombre.strip())
    return sucursal

def get_or_create_asesor(nombre, codigo, sucursal):
    if not nombre or not codigo:
        return None
    # Si hay código de asesor, buscar por ese campo
    # Buscar email en la tabla de usuarios por codigo_asesor o por nombre
    email = None
    if codigo:
        try:
            email = CustomUser.objects.get(codigo_asesor=codigo).email
        except CustomUser.DoesNotExist:
            pass
    if not email and nombre:
        try:
            email = CustomUser.objects.get(first_name=nombre.split()[0], last_name=' '.join(nombre.split()[1:])).email
        except CustomUser.DoesNotExist:
            pass
    # Si hay código de asesor, buscar por ese campo
    if codigo:
        try:
            user = CustomUser.objects.get(codigo_asesor=codigo)
            updated = False
            if email and user.username != email:
                user.username = email
                updated = True
            if user.first_name != nombre.split()[0]:
                user.first_name = nombre.split()[0]
                updated = True
            if user.last_name != ' '.join(nombre.split()[1:]):
                user.last_name = ' '.join(nombre.split()[1:])
                updated = True
            if user.sucursal != sucursal:
                user.sucursal = sucursal
                updated = True
            if not user.is_active:
                user.is_active = True
                updated = True
            if email and user.email != email:
                user.email = email
                updated = True
            if updated:
                user.save()
            return user
        except CustomUser.DoesNotExist:
            pass
    # Si no existe, crear uno nuevo
    username = email if email else (f"asesor_{codigo}" if codigo else nombre.replace(' ', '_').lower())
    user = CustomUser.objects.create(
        username=username if username else '',
        first_name=nombre.split()[0],
        last_name=' '.join(nombre.split()[1:]),
        rol='Asesor',
        sucursal=sucursal,
        is_active=True,
        codigo_asesor=codigo if codigo else None,
        email=username if '@' in username else '',
    )
    return user

def import_clients():
    with open(CSV_PATH, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sucursal = get_or_create_sucursal(row['Sucursal'])
            asesor = get_or_create_asesor(row['Asesor'], row['Codigo Asesor'], sucursal)
            client, created = Client.objects.get_or_create(
                codigo_cliente=row['Codigo Cliente'],
                sucursal=sucursal,
                defaults={
                    'nombre': row['Cliente '].strip(),
                    'asesor': asesor,
                    'codigo_asesor': row['Codigo Asesor'] if row['Codigo Asesor'] else None,
                }
            )
            # Si el cliente ya existe, actualizar asesor y código asesor si es necesario
            updated = False
            if not created:
                if client.asesor != asesor:
                    client.asesor = asesor
                    updated = True
                if client.codigo_asesor != (row['Codigo Asesor'] if row['Codigo Asesor'] else None):
                    client.codigo_asesor = row['Codigo Asesor'] if row['Codigo Asesor'] else None
                    updated = True
                if updated:
                    client.save()
            if created:
                print(f"Cliente creado: {client.nombre}")
            else:
                print(f"Cliente actualizado: {client.nombre}")

if __name__ == '__main__':
    import_clients()
