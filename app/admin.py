from django.contrib import admin
from app.models import *


admin.site.register(Item)
admin.site.register(Tax)
admin.site.register(Order)
admin.site.register(Discount)