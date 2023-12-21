from django.contrib import admin
from .models import Review, Product, Business, Image, Tag

# Register your models here.

admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Business)
admin.site.register(Image)
admin.site.register(Tag)
