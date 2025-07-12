from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    def asesor_nombre(self, obj):
        if obj.asesor:
            return f"{obj.asesor.first_name} {obj.asesor.last_name}".strip()
        return '-'
    asesor_nombre.short_description = 'Asesor'

    def asesor_codigo(self, obj):
        if obj.asesor and obj.asesor.codigo_asesor:
            return obj.asesor.codigo_asesor
        return '-'
    asesor_codigo.short_description = 'Código Asesor'

    list_display = ('nombre', 'codigo_cliente', 'sucursal', 'asesor_nombre', 'asesor_codigo', 'potential_purchase')
    search_fields = ('nombre', 'codigo_cliente', 'sucursal', 'asesor__email', 'asesor__first_name', 'asesor__last_name', 'asesor__codigo_asesor')
    ordering = ('nombre',)
    list_filter = ('sucursal', 'asesor')
    list_per_page = 25

# Registra tus modelos aquí.
