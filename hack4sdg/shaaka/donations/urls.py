from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('thanks/', views.thanks, name='thanks'),
]