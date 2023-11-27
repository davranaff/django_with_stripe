from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Item(BaseModel):
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.DecimalField(default=0, max_digits=10, decimal_places=2)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Item'
		verbose_name_plural = 'Items'


class Order(BaseModel):
	total_price = models.DecimalField(default=0, max_digits=12, decimal_places=2)

	order = models.ForeignKey('Discount', models.CASCADE, related_name='orders', related_query_name='orders')
	tax = models.ForeignKey('Tax', models.CASCADE, related_name='orders', related_query_name='orders')
	item = models.ForeignKey('Item', models.CASCADE, related_name='orders', related_query_name='orders')



	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'


class Discount(BaseModel):
	percentage = models.IntegerField(validators=[
			MaxValueValidator(100),
			MinValueValidator(0)
		])

	class Meta:
		verbose_name = 'Discount'
		verbose_name_plural = 'Discounts'


class Tax(BaseModel):
	percentage = models.IntegerField(validators=[
			MaxValueValidator(100),
			MinValueValidator(0)
		])

	class Meta:
		verbose_name = 'Tax'
		verbose_name_plural = 'Taxes'
