from django.shortcuts import render


def home(request):
    """Página principal simple."""
    return render(request, 'home.html')

