# Create your views here.
from cart.forms import CartAddItemForm
from django.views.generic.edit import FormView

from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from django.http import HttpResponseRedirect
from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin




class CartAddView(SuccessMessageMixin, FormView):
    template_name = 'item/detail.html'
    form_class = CartAddItemForm
    success_url = reverse_lazy('item_list')
    success_message = "You have successfully added item to cart"


  

    def form_valid(self, form):
        self.add_to_cart(form.cleaned_data)
        return super().form_valid(form)

    def add_to_cart(self, valid_data):
        #print(self.request)
        #Send mail to admin with valid_data['order'] and valid_data['user_name']
        #print(valid_data)
        cart = Cart(self.request)
        item = get_object_or_404(Item, id=valid_data['item_id'])
        update = None,
        if int(valid_data['update']) == 0:
            update = False
        
        if int(valid_data['update']) == 1:
            update = True
        cart.add(item=item,
                    quantity=int(valid_data['quantity']),
                    update_quantity = update
                    )



class CartAddView2(View):
   
    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        cart = Cart(request)
        #cart.clear()
        #cart = Cart(request)
        
        item = get_object_or_404(Item, id=data['item_id'])
        cart.add(item=item,
                    quantity=int(data['quantity']),
                    )
        #return HttpResponseRedirect('/success/')
        return redirect('item_detail')

        #return render(request, self.template_name, {'form': form})



def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})




class CartDetailView(View):
    template_name = 'cart/detail.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, self.template_name, {'cart': cart})



#def cart_remove(request, product_id):
#cart = Cart(request)
#product = get_object_or_404(Product, id=product_id)
#cart.remove(product)
#return redirect('cart:cart_detail')


class CartRemoveView(View):
    template_name = 'cart/detail.html'

    def get(self, request, *args, **kwargs):
        #print(kwargs)
        cart = Cart(request)
        item = get_object_or_404(Item, id=kwargs['id'])
        cart.remove(item)
        #return render(request, self.template_name, {'cart': cart})
        return redirect('cart_detail')