from django.urls import reverse

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_images')
    price = models.IntegerField()
    category = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name