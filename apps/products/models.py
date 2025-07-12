from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit_of_measure = models.CharField(max_length=50, default='litros')

    def __str__(self):
        return self.name
