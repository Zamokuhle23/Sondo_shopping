from django.shortcuts import render, redirect
from django.views import View
from store.models import Customer
from store.models import Order



class OrderView(View):
    def get(self, request):
        customer_id = Customer.objects.get(customer=self.request.user)
        orders = Order.objects.all()
        print(orders)
        return render(request, 'order.html', {"orders": orders})
