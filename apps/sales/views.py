from django.shortcuts import render

from .models import Quote, Sale

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'sales/quote_list.html', {"quotes": quotes})

def quote_detail(request, pk):
    quote = Quote.objects.get(pk=pk)
    return render(request, 'sales/quote_detail.html', {"quote": quote})

def quote_form(request):
    return render(request, 'sales/quote_form.html')


def sale_list(request):
    sales = Sale.objects.all()[:50]
    return render(request, 'sales/sale_list.html', {"sales": sales})
