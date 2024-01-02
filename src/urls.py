from django.urls import path
from .import views

app_name = 'src'

urlpatterns = [
    path('', views.product_list, name='product_list'),  # 상품 목록
    path('basket/', views.basket_list, name='basket_list'),  # 장바구니 목록

    path('basket/add/<int:product_id>/', views.basket_add, name='add'),  # 장바구니 담기

    path('basket/<int:order_id>/plus/', views.basket_plus, name='plus'),  # 장바구니 수량 변경
    path('basket/<int:order_id>/minus/', views.basket_minus, name='minus'),  # 장바구니 수량 변경
]
