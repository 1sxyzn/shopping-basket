from django.db import models


class Product(models.Model):
    name = models.TextField()
    desc = models.TextField()
    price = models.IntegerField()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cnt = models.IntegerField(default=0)


class Basket(models.Model):
    order = models.ManyToManyField(Order)
