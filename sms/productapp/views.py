from django.shortcuts import render

from productapp.models import Product
from productapp.forms import ProductForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'productapp/home.html')

def view_stock(request):
    products = Product.objects.all()
    return render(request, 'productapp/stock.html', {'products': products})

def view_products(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'productapp/products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()

    return render(request, 'productapp/add_product.html', {'form': form})