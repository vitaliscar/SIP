from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('form/', views.goal_form, name='goal_form'),
    path('fulfillment/', views.goal_fulfillment, name='goal_fulfillment'),
]
