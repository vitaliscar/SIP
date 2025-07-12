import csv
from django.core.management.base import BaseCommand
from apps.clients.models import Client, Sucursal
from apps.users.models import CustomUser

class Command(BaseCommand):
    help = 'Carga clientes desde un archivo CSV y vincula asesor y sucursal por nombre.'

    def handle(self, *args, **options):
        with open('d:/Users/v52anap/Downloads/Ficha Maestra CCV - Listado de clientes.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sucursal_nombre = row['Sucursal'].strip()
                sucursal = Sucursal.objects.filter(nombre__iexact=sucursal_nombre).first()
                nombre = row['Cliente '].strip()
                codigo_cliente = row['Codigo Cliente'].strip()
                asesor_nombre = row['Asesor'].strip() if row['Asesor'] else None
                codigo_asesor = row['Codigo Asesor'].strip() if row['Codigo Asesor'] else None
                asesor = None
                if codigo_asesor:
                    asesor = CustomUser.objects.filter(codigo_asesor=codigo_asesor).first()
                client, created = Client.objects.get_or_create(
                    codigo_cliente=codigo_cliente,
                    defaults={
                        'sucursal': sucursal,
                        'nombre': nombre,
                        'asesor': asesor,
                        'codigo_asesor': codigo_asesor,
                    }
                )
                if not sucursal:
                    self.stdout.write(self.style.ERROR(f'Sucursal no encontrada: {sucursal_nombre}'))
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Creado: {nombre} ({codigo_cliente})'))
                else:
                    client.sucursal = sucursal
                    client.nombre = nombre
                    client.asesor = asesor
                    client.codigo_asesor = codigo_asesor
                    client.save()
                    self.stdout.write(self.style.WARNING(f'Actualizado: {nombre} ({codigo_cliente})'))
        self.stdout.write(self.style.SUCCESS('Carga de clientes finalizada.'))
