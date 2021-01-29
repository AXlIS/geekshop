from django.conf import settings
from django.db import models

# Create your models here.
from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PROCEED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    DONE = 'DN'
    CANCEL = 'CNC'

    ORDER_STATUSES = (
        (FORMING, 'Формируется'),
        (SEND_TO_PROCEED, 'Отправлен в обработку'),
        (PROCEED, 'Обработан'),
        (PAID, 'Оплачен'),
        (READY, 'Готов'),
        (DONE, 'Выдан'),
        (CANCEL, 'Отменен')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cоздан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    status = models.CharField(choices=ORDER_STATUSES, verbose_name='Статус', max_length=3, default=FORMING)
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at', )

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        total_quantity = sum(list(map(lambda x: x.quantity, items)))
        return total_quantity

    def get_total_cost(self):
        items = self.orderitems.select_related()
        total_cost = sum(list(map(lambda x: x.quantity * x.product.price, items)))
        return total_cost

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Колличество')

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()