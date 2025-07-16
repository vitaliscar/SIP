
from django.db.models import Sum
from apps.clients.models import Client, PotencialDeCompra

def run():
    print('Clientes con potenciales:')
    for c in Client.objects.all():
        total = PotencialDeCompra.objects.filter(cliente=c).aggregate(Sum('potencial'))['potencial__sum'] or 0
        print(f'{c.nombre}: {total} L')
        print('--- Detalle por producto ---')
        for p in PotencialDeCompra.objects.filter(cliente=c):
            print(f'  {p.producto.name}: {p.potencial} L')
