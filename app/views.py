from django.shortcuts import render, redirect
# from rest_framework.views import APIView
from django.views import View
from app.models import Item
from django.shortcuts import get_object_or_404
from django.conf import settings
import stripe



class ItemsPage(View):
	template_name = 'home.html'

	def get(self, request):
		items = Item.objects.all()
		return render(request, self.template_name, {'items': items})


class BuyApi(View):

	def get(self, request, id):
		item = get_object_or_404(Item, pk=id)

		stripe.api_key = settings.STRIPE_API_KEY

		session = stripe.checkout.Session.create(
				line_items=[{
			      	'price_data': {
			        	'currency': 'usd',
			        	'product_data': {
			        		  'name': item.name,
		        			},
			        	'unit_amount': int(item.price),
			      	},
			      	'quantity': 1,
			    }],
			    mode='payment',
			    success_url='http://localhost:8000/v1/app/success',
			    cancel_url='http://localhost:8000/v1/app/cancel',
			)

		return redirect(session.url, code=303)

		# session =stripe.PaymentIntent.create(
		# 	  amount=int(item.price),
		# 	  currency="usd",
		# 	  description=item.description,
		# 	  automatic_payment_methods={"enabled": True}
		# 	)

		# print(session)


class ItemTemplate(View):
	template_name = "item.html"

	def get(self, request, pk):
		item = get_object_or_404(Item, pk=pk)
		return render(request, self.template_name, {'item': item})


def success_page(request):
	return render(request, 'success.html', {'info': None})


def cancel_page(request):
	return render(request, 'cancel.html', {'info': None})