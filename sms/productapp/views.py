from django.shortcuts import render

from productapp.models import Product
from productapp.forms import ProductForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'productapp/home.html')

@login_required(login_url='login')
def view_stock(request):
    query = request.GET.get('q', '')  

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(category__name__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'productapp/stock.html', {
        'products': products,
        'query': query
    })
@login_required(login_url='login')
def view_products(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'productapp/products.html', {'products': products})

@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()

    return render(request, 'productapp/add_product.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'productapp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'productapp/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')