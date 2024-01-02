from django.db import models


class Product(models.Model):
    name = models.TextField()
    desc = models.TextField()
    price = models.IntegerField()
    sale = models.IntegerField(default=0)
    sale_price = models.IntegerField()  # 할인이 적용된 가격
    img = models.TextField(default="")  # 이미지 링크 저장


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cnt = models.IntegerField(default=0)


class Basket(models.Model):
    order = models.ManyToManyField(Order)
