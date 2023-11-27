from django.urls import path
from app.views import ItemTemplate, BuyApi, ItemsPage, success_page, cancel_page

urlpatterns = [
	path('', ItemsPage.as_view(), name='home'),
	path('cancel/', cancel_page, name='cancel'),
	path('success/', success_page, name='success'),
	path('buy/<int:id>', BuyApi.as_view(), name='buy'),
	path('item/<int:pk>', ItemTemplate.as_view(), name='item'),
]