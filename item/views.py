from django_filters.views import FilterView
from django.views.generic import DetailView

from item import models, filters



class ItemListView(FilterView):
    template_name = "item/list.html"
    context_object_name = 'items'  # Default: object_list
    paginate_by = 5
    filterset_class= filters.ItemFilter

   
class ItemDetailView(DetailView):
    model = models.Item
    template_name = 'item/detail.html'
    context_object_name = 'item'