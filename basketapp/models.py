from django.db import models
from django.utils.functional import cached_property

from authapp.models import User
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    @cached_property
    def get_item_cashed(self):
        return self.user.basket.select_related()

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = self.get_item_cashed
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_item_cashed
        return sum(basket.sum() for basket in baskets)

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()
