from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Sucursal

def client_list(request):
    from .models import Client
    from django.db.models import Sum
    clients = Client.objects.all().annotate(
        aggregate_total=Sum('potenciales__potencial')
    ).order_by('nombre')
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    from .models import Client
    from django.db.models import Sum
    client = Client.objects.prefetch_related('potenciales__producto').get(pk=pk)
    potenciales = client.potenciales.select_related('producto').all()
    potencial_total = potenciales.aggregate(total=Sum('potencial'))['total']
    return render(request, 'clients/client_detail.html', {
        'client': client,
        'potenciales': potenciales,
        'potencial_total': potencial_total,
    })

def client_form(request):
    from .forms import ClientForm
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'clients/client_form.html', {'form': form, 'success': True})
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})

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
