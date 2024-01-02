from django.urls import path
from .import views

app_name = 'src'

urlpatterns = [
    path('main/', views.product_list, name='product_list'),
    path('basket/', views.basket_list, name='basket_list'),
]
