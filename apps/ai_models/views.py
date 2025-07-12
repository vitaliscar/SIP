from django.shortcuts import render

# Define tus vistas aquí.

# Definir la vista forecast_results
def forecast_results(request):
    return render(request, 'ai_models/forecast_results.html')
