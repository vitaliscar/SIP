from django.contrib import admin

from .models import Quote, Sale


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("name", "total")


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("numero_factura", "compania", "sucursal", "cantidad")
