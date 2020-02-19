from django.urls import path, include

from item.views import ItemListView, ItemDetailView
from cart.views import CartAddView, cart_detail, CartDetailView, CartRemoveView
from django.conf.urls.i18n import i18n_patterns
from order.views import OrderAddView
from payment.views import PaymentView



urlpatterns = [
        path('', ItemListView.as_view(), name='item_list'),
        path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
        path('cart/', CartAddView.as_view(), name='cart_add'),
        path('cart/detail/', CartDetailView.as_view(), name='cart_detail'),
        path('cart/remove/<int:id>/', CartRemoveView.as_view(), name='cart_remove'),
        path('order/', OrderAddView.as_view(), name='order_add'),
        path('payment/', PaymentView.as_view(), name='payment_do'),

] 

