import csv
import os
import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()
from apps.users.models import CustomUser
from apps.clients.models import Sucursal

def run():
    csv_file_path = r'd:\Users\v52anap\Documents\sales_intelligence_platform\Datos\Ficha Maestra CCV - Asesores (4).csv'
    with open(csv_file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        print(f"Columnas detectadas: {reader.fieldnames}")
        for row in reader:
            codigo_asesor = row.get('Codigo Asesor', '').strip()
            nombre_asesor = row.get('Asesor', '').strip()
            sucursal_nombre = row.get('Sucursal', '').strip()
            sucursal_inst = None
            if sucursal_nombre:
                sucursal_inst = Sucursal.objects.filter(nombre__iexact=sucursal_nombre).first()
            username = row.get('Email', '').strip()  # Usar siempre el email como username
            email = row.get('Email', '').strip()
            rol = row.get('Rol', '').strip()
            if not nombre_asesor or not username:
                continue
            # Si el rol no es 'Asesor', no asignar codigo_asesor
            if rol.lower() != 'asesor':
                codigo_asesor = None
            # Separar nombre y apellido
            partes_nombre = nombre_asesor.split()
            first_name = partes_nombre[0] if partes_nombre else ''
            last_name = ' '.join(partes_nombre[1:]) if len(partes_nombre) > 1 else ''
            user, created = CustomUser.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'codigo_asesor': codigo_asesor,
                    'sucursal': sucursal_inst,
                    'rol': rol,
                }
            )
            # Si ya existe, actualizar datos
            if not created:
                cambios = False
                if user.username != username:
                    user.username = username
                    cambios = True
                if user.first_name != first_name:
                    user.first_name = first_name
                    cambios = True
                if user.last_name != last_name:
                    user.last_name = last_name
                    cambios = True
                if user.email != email:
                    user.email = email
                    cambios = True
                # Solo actualizar codigo_asesor si el rol es Asesor
                if rol.lower() == 'asesor' and user.codigo_asesor != codigo_asesor:
                    user.codigo_asesor = codigo_asesor
                    cambios = True
                if hasattr(user, 'sucursal') and user.sucursal != sucursal_inst:
                    user.sucursal = sucursal_inst
                    cambios = True
                if hasattr(user, 'rol') and user.rol != rol:
                    user.rol = rol
                    cambios = True
                if cambios:
                    user.save()
            print(f"Asesor registrado: {first_name} {last_name} | Usuario: {username} | Email: {email} | Código: {codigo_asesor} | Sucursal: {sucursal_nombre} | Rol: {rol} | {'Nuevo' if created else 'Actualizado'}")
