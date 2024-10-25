from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm
from .models import Product

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('farmers:product_list')
    else:
        form = UserCreationForm()
    return render(request, 'farmers/register.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            return redirect('farmers:product_list')
    else:
        form = ProductForm()
    return render(request, 'farmers/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.filter(farmer=request.user)
    return render(request, 'farmers/product_list.html', {'products': products})