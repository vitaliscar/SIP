from django.urls import path
from . import views

app_name = 'ai_models'

urlpatterns = [
    path('forecast/', views.forecast_results, name='forecast_results'),
]
