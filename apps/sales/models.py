from django.db import models

class Quote(models.Model):
    name = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
