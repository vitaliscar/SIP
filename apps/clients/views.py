from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Sucursal

def client_list(request):
    return render(request, 'clients/client_list.html')

def client_detail(request, pk):
    return render(request, 'clients/client_detail.html')

def client_form(request):
    return render(request, 'clients/client_form.html')

class SucursalListView(ListView):
    model = Sucursal
    template_name = 'clients/sucursal_list.html'
    context_object_name = 'sucursales'

class SucursalDetailView(DetailView):
    model = Sucursal
    template_name = 'clients/sucursal_detail.html'
    context_object_name = 'sucursal'

class SucursalCreateView(CreateView):
    model = Sucursal
    fields = ['nombre']
    template_name = 'clients/sucursal_form.html'
    success_url = reverse_lazy('sucursal_list')

class SucursalUpdateView(UpdateView):
    model = Sucursal
    fields = ['nombre']
    template_name = 'clients/sucursal_form.html'
    success_url = reverse_lazy('sucursal_list')
