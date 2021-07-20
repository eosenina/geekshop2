from django.db import models
from django.utils.functional import cached_property

from authapp.models import User
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    @property
    def final_price(self):
        return self.quantity * self.product.price

    @property
    def total_quantity(self):
        items = self.get_items_cached
        total_count = 0
        # for bask in Basket.objects.filter(user=self.user):
        for bask in items:
            total_count += bask.quantity
        return total_count

    @property
    def total_sum(self):
        items = self.get_items_cached
        return sum(list(map(lambda bask: bask.quantity * bask.product.price, items)))
        # return sum(list(map(lambda bask: bask.final_price, Basket.objects.filter(user=self.user).select_related('product'))))

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)

    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.objects.get(pk=self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

