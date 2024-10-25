from django.urls import path
from . import views

app_name = 'farmers'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),
]