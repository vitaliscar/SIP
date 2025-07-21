from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.quote_list, name='quote_list'),
    path('<int:pk>/', views.quote_detail, name='quote_detail'),
    path('form/', views.quote_form, name='quote_form'),
    path('sales/', views.sale_list, name='sale_list'),
]
