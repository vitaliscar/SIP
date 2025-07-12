from django.test import TestCase
from .models import Sucursal

class SucursalModelTest(TestCase):
    def test_creacion_sucursal(self):
        sucursal = Sucursal.objects.create(nombre="Sucursal Test")
        self.assertEqual(sucursal.nombre, "Sucursal Test")
