from django.shortcuts import render, get_object_or_404, redirect
from .models import *

app_name = 'src'


def product_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
    return render(request, 'product_list.html', context)


def basket_list(request):
    # 현재는 유저 1명만 있다고 생각하여 장바구니도 1개만 이용
    # 확장하려면 유저 테이블 추가 후, 유저에 해당하는 장바구니의 pk를 가져와야함
    basket = Basket.objects.get(pk=1)
    order = basket.order.all()
    total = 0
    for o in order:
        total = total + (o.product.sale_price * o.cnt)
    context = {'orders': order, 'total': total}
    return render(request, 'basket_list.html', context)


def basket_plus(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.cnt = order.cnt + 1
    order.save()
    return redirect('src:basket_list')


def basket_minus(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.cnt = order.cnt - 1
    order.save()
    if order.cnt == 0:
        order.delete()
    return redirect('src:basket_list')


def basket_add(request, product_id):
    # user 테이블을 만들지 않았으므로 'pk=1인 basket'을 이용함 -> 이후 확장하려면 '해당 user의 basket'을 이용해야 함
    basket = Basket.objects.get(pk=1)

    # 1. order에 해당 product가 있으면 -> 해당 order의 cnt 추가
    for order in basket.order.all():
        if order.product.id == product_id:
            order.cnt = order.cnt + 1
            order.save()
            return redirect('src:product_list')

    # 2. order에 해당 product가 없으면 -> order 생성 -> basket에 order 추가
    product = Product.objects.get(pk=product_id)
    order = Order(product=product, cnt=1)
    order.save()
    basket.order.add(order)
    basket.save()
    return redirect('src:product_list')
