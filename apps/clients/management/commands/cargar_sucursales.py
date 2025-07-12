from django.core.management.base import BaseCommand
from apps.clients.models import Sucursal, SUCURSALES_PREDEFINIDAS

class Command(BaseCommand):
    help = 'Carga las sucursales predefinidas en la base de datos.'

    def handle(self, *args, **options):
        for nombre in SUCURSALES_PREDEFINIDAS:
            obj, created = Sucursal.objects.get_or_create(nombre=nombre)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Sucursal creada: {nombre}'))
            else:
                self.stdout.write(self.style.WARNING(f'Sucursal ya existe: {nombre}'))
        self.stdout.write(self.style.SUCCESS('Carga de sucursales finalizada.'))
