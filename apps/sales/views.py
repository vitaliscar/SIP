from django.shortcuts import render

def quote_list(request):
    return render(request, 'sales/quote_list.html')

def quote_detail(request, pk):
    return render(request, 'sales/quote_detail.html')

def quote_form(request):
    return render(request, 'sales/quote_form.html')
