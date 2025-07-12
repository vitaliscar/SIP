from django.urls import path
from . import views
from .views import SucursalListView, SucursalDetailView, SucursalCreateView, SucursalUpdateView

app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('form/', views.client_form, name='client_form'),
    path('sucursales/', SucursalListView.as_view(), name='sucursal_list'),
    path('sucursales/nueva/', SucursalCreateView.as_view(), name='sucursal_create'),
    path('sucursales/<int:pk>/', SucursalDetailView.as_view(), name='sucursal_detail'),
    path('sucursales/<int:pk>/editar/', SucursalUpdateView.as_view(), name='sucursal_update'),
]
