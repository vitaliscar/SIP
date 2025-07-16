import csv
import os
import django
import sys

# Configura el entorno Django
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.users.models import CustomUser
from apps.clients.models import Sucursal

CSV_PATH = r'd:\Users\v52anap\Downloads\Ficha Maestra CCV - Asesores (1).csv'

def get_or_create_sucursal(nombre):
    if not nombre:
        return None
    sucursal, _ = Sucursal.objects.get_or_create(nombre=nombre.strip())
    return sucursal

def import_users():
    with open(CSV_PATH, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sucursal = get_or_create_sucursal(row['Sucursal'])
            username = row['Email']  # El username siempre será el email
            codigo_asesor = row['Codigo Asesor'] if row['Codigo Asesor'] else None
            user = None
            created = False
            # Buscar por codigo_asesor si existe
            if codigo_asesor:
                try:
                    user = CustomUser.objects.get(codigo_asesor=codigo_asesor)
                except CustomUser.DoesNotExist:
                    pass
            # Si no existe por codigo_asesor, buscar por username/email
            if user is None:
                try:
                    user = CustomUser.objects.get(username=username)
                except CustomUser.DoesNotExist:
                    pass
            # Si no existe, crearlo
            if user is None:
                user = CustomUser.objects.create(
                    username=username,
                    first_name=row['Asesor'].split()[0],
                    last_name=' '.join(row['Asesor'].split()[1:]),
                    email=row['Email'],
                    rol=row['Rol'],
                    sucursal=sucursal,
                    is_active=True,
                    codigo_asesor=codigo_asesor,
                )
                created = True
            else:
                updated = False
                if user.username != username:
                    user.username = username
                    updated = True
                if user.first_name != row['Asesor'].split()[0]:
                    user.first_name = row['Asesor'].split()[0]
                    updated = True
                if user.last_name != ' '.join(row['Asesor'].split()[1:]):
                    user.last_name = ' '.join(row['Asesor'].split()[1:])
                    updated = True
                if user.email != row['Email']:
                    user.email = row['Email']
                    updated = True
                if user.rol != row['Rol']:
                    user.rol = row['Rol']
                    updated = True
                if user.sucursal != sucursal:
                    user.sucursal = sucursal
                    updated = True
                if user.codigo_asesor != codigo_asesor:
                    user.codigo_asesor = codigo_asesor
                    updated = True
                if updated:
                    user.save()
            print(f"{'Creado' if created else 'Actualizado'}: {user.username} - {user.rol} - {user.codigo_asesor}")

if __name__ == '__main__':
    import_users()
