from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from order.forms import OrderCreateForm
from order.models import Order, OrderItem
from django.views.generic.edit import CreateView




class OrderAddView(SuccessMessageMixin, CreateView):
    template_name = 'order/add.html'
    model = Order
    fields = ['email']
    success_url = reverse_lazy('payment_do')
    success_message = "You have successfully place order"
  

    def form_valid(self, form):
        #self.process(form.cleaned_data)
        cart = Cart(self.request)
        order = form.save()
        for line in cart:
            OrderItem.objects.create(order=order,
                item=line['item'],
                price=line['price'],
                quantity=line['quantity'])
        # clear the cart
        cart.clear()
        self.request.session['order_id'] = order.id
        return super().form_valid(form)



    def process(self, valid_data):
        #print(self.request)
        #Send mail to admin with valid_data['order'] and valid_data['user_name']
        #print(valid_data)
        pass
      