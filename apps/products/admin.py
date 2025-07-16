from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('cod_chronus', 'cod_ccv', 'name', 'calidad_categoria', 'uso', 'unidad_empaque', 'litros_unidad', 'lts', 'unidades_x_ue', 'venta_detalle')
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

# Registra tus modelos aquí.
