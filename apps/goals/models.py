from django.db import models

class SalesGoal(models.Model):
    name = models.CharField(max_length=255)
    target = models.DecimalField(max_digits=10, decimal_places=2)
    sucursal = models.ForeignKey('clients.Sucursal', on_delete=models.CASCADE, related_name='metas')

    def __str__(self):
        return self.name
