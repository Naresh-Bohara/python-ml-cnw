from django.shortcuts import render

from productapp.models import Product

# Create your views here.
def home(request):
    return render(request, 'productapp/home.html')

def view_stock(request):
    products = Product.objects.all()
    return render(request, 'productapp/stock.html', {'products': products})