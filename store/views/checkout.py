from django.shortcuts import render, redirect
from django.views import View
from store.models import Order
from store.models import Customer
from store.models import Product
from store.tasks import OrderEmail


class Checkout(View):
	def get(self,request):
		return redirect('cart')

	def post(self,request):
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		cart = request.session.get('cart')
		products = Product.getProductById(list(cart.keys()))
		customer = request.session.get('customer')

		for product in products:

			newOrder = Order(
					product=product,
					customer=Customer(id=customer),
					quantity=cart[str(product.id)],
					price=product.price,
					address=address,
					phone=phone,
				)
			newOrder.save()
			print(customer)
			OrderEmail.delay(order_id=newOrder.id)

		request.session['cart'] = {}
		return redirect('order')
