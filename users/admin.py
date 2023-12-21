from django.contrib import admin
from .models import Seller, Buyer, ShoppingCart

# Register your models here.

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(ShoppingCart)
