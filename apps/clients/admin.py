from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db import models
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    def mostrar_asesor_nombre(self, obj):
        # Prioridad: nombre del usuario relacionado, si no, el del modelo
        if obj.asesor:
            nombre = f"{obj.asesor.first_name} {obj.asesor.last_name}".strip()
            return nombre if nombre else obj.asesor_nombre or '-'
        return obj.asesor_nombre or '-'
    mostrar_asesor_nombre.short_description = 'Asesor'

    def mostrar_codigo_asesor(self, obj):
        # Prioridad: código del usuario relacionado, si no, el del modelo
        if obj.asesor and obj.asesor.codigo_asesor:
            return obj.asesor.codigo_asesor
        return obj.codigo_asesor or '-'
    mostrar_codigo_asesor.short_description = 'Código Asesor'

    def potencial_total(self, obj):
        total = obj.potenciales.aggregate(total=models.Sum('potencial'))['total']
        return total if total is not None else 0
    potencial_total.short_description = 'Potencial Total (L)'

    def ver_detalle_potenciales(self, obj):
        url = reverse('admin:detalle_potenciales_cliente', args=[obj.pk])
        return format_html('<a href="{}">Ver detalle</a>', url)
    ver_detalle_potenciales.short_description = 'Detalle Potenciales'

    list_display = ('nombre', 'codigo_cliente', 'sucursal', 'mostrar_asesor_nombre', 'mostrar_codigo_asesor', 'potencial_total', 'ver_detalle_potenciales')
    search_fields = ('nombre', 'codigo_cliente', 'sucursal__nombre', 'asesor__email', 'asesor__first_name', 'asesor__last_name', 'asesor__codigo_asesor', 'asesor_nombre', 'codigo_asesor')
    ordering = ('nombre',)
    list_filter = ('sucursal', 'asesor')
    list_per_page = 25
    # Mostrar ambos campos en el formulario
    fields = ('nombre', 'codigo_cliente', 'sucursal', 'asesor', 'asesor_nombre', 'codigo_asesor')

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('detalle-potenciales/<int:cliente_id>/', self.admin_site.admin_view(self.detalle_potenciales_view), name='detalle_potenciales_cliente'),
        ]
        return custom_urls + urls

    def detalle_potenciales_view(self, request, cliente_id):
        from django.shortcuts import render, get_object_or_404
        cliente = get_object_or_404(Client, pk=cliente_id)
        potenciales = cliente.potenciales.select_related('producto').all()
        return render(request, 'admin/clients/detalle_potenciales.html', {
            'cliente': cliente,
            'potenciales': potenciales,
        })

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
