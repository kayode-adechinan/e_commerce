from django.shortcuts import render, redirect, get_object_or_404

from order.models import Order

from django.contrib import messages

from django.views import View




# Create your views here.
class PaymentView(View):
    template_name = 'payment/pay.html'

    def get(self, request, *args, **kwargs):  


        action = request.GET.get('action')

        if action is None:
            
            return render(request, self.template_name)

        
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, id=order_id)    
        order.paid = True
        order.save()
        messages.success(request, 'You successfully paid!') 

        return redirect('item_list')




