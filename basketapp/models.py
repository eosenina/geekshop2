from functools import reduce

from django.db import models
from authapp.models import User
from mainapp.models import Product


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    @property
    def final_price(self):
        return self.quantity * self.product.price

    @property
    def total_quantity(self):
        total_count = 0
        for bask in Basket.objects.filter(user=self.user):
            total_count += bask.quantity
        return total_count

    @property
    def total_sum(self):
        return sum(list(map(lambda bask: bask.final_price, Basket.objects.filter(user=self.user))))
