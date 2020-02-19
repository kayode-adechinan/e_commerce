# Create your views here.
from rest_framework import viewsets
from item import models, serializers, filters


# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    filterset_class = filters.ItemFilter
