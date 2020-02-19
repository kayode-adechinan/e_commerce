from django.db import models
from item.models import Item

# Create your models here.

class Order(models.Model):
    email = models.EmailField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='order_items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity