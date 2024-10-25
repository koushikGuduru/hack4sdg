from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import FoodItemForm
from .models import FoodItem

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homemakers:food_list')
    else:
        form = UserCreationForm()
    return render(request, 'homemakers/register.html', {'form': form})

def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.homemaker = request.user
            food_item.save()
            return redirect('homemakers:food_list')
    else:
        form = FoodItemForm()
    return render(request, 'homemakers/add_food_item.html', {'form': form})

def food_list(request):
    food_items = FoodItem.objects.filter(homemaker=request.user)
    return render(request, 'homemakers/food_list.html', {'food_items': food_items})