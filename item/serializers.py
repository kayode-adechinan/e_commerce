from rest_framework import serializers
from item.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "image",
            "price",
            "category",
           
        )
        model = Item
