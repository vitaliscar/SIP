from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unit_of_measure')
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25

# Registra tus modelos aquí.
