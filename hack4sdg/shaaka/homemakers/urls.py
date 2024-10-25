from django.urls import path
from . import views

app_name = 'homemakers'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
    path('food_list/', views.food_list, name='food_list'),
]