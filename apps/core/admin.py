from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html

class CustomAdminSite(AdminSite):
    site_header = 'Sales Intelligence Platform'
    site_title = 'Sales Intelligence Admin'
    index_title = 'Panel de administración'

    def each_context(self, request):
        context = super().each_context(request)
        context['site_logo'] = '/static/css/REFRESH LOGO.png'
        context['site_favicon'] = '/static/css/REFRESH LOGO.png'
        return context

admin_site = CustomAdminSite()

# Si tienes modelos personalizados, regístralos aquí con admin_site.register()
