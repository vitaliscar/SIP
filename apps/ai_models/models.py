from django.db import models

class AIModelConfig(models.Model):
    name = models.CharField(max_length=255)
    configuration = models.JSONField()

    def __str__(self):
        return self.name
