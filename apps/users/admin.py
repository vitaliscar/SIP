from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    def nombre_completo(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()
    nombre_completo.short_description = 'Nombre'

    def codigo_asesor_display(self, obj):
        return obj.codigo_asesor if obj.codigo_asesor else '-'
    codigo_asesor_display.short_description = 'Codigo asesor'

    def rol_display(self, obj):
        return obj.rol if obj.rol else '-'
    rol_display.short_description = 'Rol'

    list_display = (
        'nombre_completo',
        'username',
        'email',
        'codigo_asesor_display',
        'sucursal',
        'rol_display',
        'is_active',
        'is_staff',
    )
    list_filter = ('sucursal', 'rol', 'is_active', 'is_staff')
    search_fields = (
        'first_name',
        'last_name',
        'username',
        'email',
        'codigo_asesor',
    )
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Datos de Asesor', {'fields': ('codigo_asesor', 'sucursal', 'rol', 'first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'codigo_asesor', 'sucursal', 'rol', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    list_per_page = 25

    readonly_fields = ()  # Asegura que ningún campo sea solo lectura

    def get_readonly_fields(self, request, obj=None):
        # Permite editar todos los campos al crear y editar usuarios
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        obj.username = obj.email  # El usuario siempre será el correo
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        # Permite que el admin pueda editar cualquier usuario
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        # Permite que el admin pueda ver cualquier usuario
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        # Permite que el admin pueda eliminar cualquier usuario
        return request.user.is_superuser or request.user.is_staff

    def has_add_permission(self, request):
        # Permite que el admin pueda agregar usuarios
        return request.user.is_superuser or request.user.is_staff
