from django.shortcuts import render
from .models import *

app_name = 'src'


def product_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
    return render(request, 'product_list.html', context)


def basket_list(request):
    basket = Basket.objects.get(pk=1)
    order = basket.order.all()
    total = 0
    for o in order:
        total = total + (o.product.price * o.cnt)
    context = {'orders': order, 'total': total}
    return render(request, 'basket_list.html', context)
