from django.shortcuts import render

def product_list(request):
    return render(request, 'products/product_list.html')

def product_detail(request, pk):
    return render(request, 'products/product_detail.html')

def product_form(request):
    return render(request, 'products/product_form.html')
