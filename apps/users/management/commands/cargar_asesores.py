import csv
from django.core.management.base import BaseCommand
from apps.users.models import CustomUser
from apps.clients.models import Sucursal

class Command(BaseCommand):
    help = 'Carga usuarios desde un archivo CSV y vincula sucursal por nombre.'

    def handle(self, *args, **options):
        with open('d:/Users/v52anap/Downloads/Ficha Maestra CCV - Asesores (1).csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                codigo = row.get('Codigo Asesor') or None
                nombre = row['Asesor']
                sucursal_nombre = row['Sucursal'].strip()
                sucursal = Sucursal.objects.filter(nombre__iexact=sucursal_nombre).first()
                email = row['Email']
                rol = row['Rol']
                username = email
                user = None
                if codigo:
                    user = CustomUser.objects.filter(codigo_asesor=codigo).first()
                if not user:
                    user = CustomUser.objects.filter(email=email).first()
                if user:
                    user.username = email
                    user.first_name = nombre.split()[0]
                    user.last_name = ' '.join(nombre.split()[1:])
                    user.sucursal = sucursal
                    user.rol = rol
                    user.is_active = True
                    user.save()
                    self.stdout.write(self.style.WARNING(f'Actualizado: {nombre} ({email})'))
                else:
                    user = CustomUser(
                        username=email,
                        email=email,
                        first_name=nombre.split()[0],
                        last_name=' '.join(nombre.split()[1:]),
                        codigo_asesor=codigo,
                        sucursal=sucursal,
                        rol=rol,
                        is_active=True,
                    )
                    user.set_password('asesor123')
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f'Creado: {nombre} ({email})'))
        self.stdout.write(self.style.SUCCESS('Carga de usuarios finalizada.'))
