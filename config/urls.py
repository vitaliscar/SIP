from django.contrib import admin
from django.urls import path, include
from apps.core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('clients/', include('apps.clients.urls')),
    path('products/', include('apps.products.urls')),
    path('sales/', include('apps.sales.urls')),
    path('goals/', include('apps.goals.urls')),
    path('reporting/', include('apps.reporting.urls')),
    path('ai_models/', include('apps.ai_models.urls')),
    path('', home, name='home'),
]
