from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stock/', views.view_stock, name='view_stock'),
     path('products/', views.view_products, name='view_products'),
]