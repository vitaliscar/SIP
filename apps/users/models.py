from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    codigo_asesor = models.CharField(max_length=10, blank=True, null=True, unique=True)
    sucursal = models.ForeignKey('clients.Sucursal', null=True, blank=True, on_delete=models.SET_NULL, related_name='usuarios')
    rol = models.CharField(max_length=30, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
