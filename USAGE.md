# Ejemplos de uso básico de SIP

## Crear un cliente desde el shell de Django
```python
from apps.clients.models import Client
Client.objects.create(nombre="Empresa Ejemplo", codigo_cliente="C1234")
```

## Importar ventas desde CSV
```bash
python manage.py import_sales path/to/archivo.csv
```

## Crear una sucursal
```python
from apps.clients.models import Sucursal
Sucursal.objects.create(nombre="Sucursal Centro")
```

## Consultar clientes por sucursal
```python
from apps.clients.models import Sucursal
sucursal = Sucursal.objects.get(nombre="Sucursal Centro")
clientes = sucursal.clientes.all()
```
