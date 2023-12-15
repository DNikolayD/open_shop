from django.db.models import (Model as DbModel, OneToOneField as One, CharField, EmailField, DateTimeField, UUIDField,
                              ManyToManyField as Many, IntegerField, CASCADE)
from products.models import Review, Product
from django.contrib.auth.models import User
from uuid import uuid4 as id_type

# Create your models here.


class Seller(DbModel):
    user = One(User, on_delete=CASCADE, null=True, blank=True)
    name = CharField(max_length=200)
    phone = CharField(max_length=13)
    email = EmailField(max_length=500, blank=True, null=True)
    reviews = Many(to=Review, blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    id = UUIDField(default=id_type, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']


class Buyer(DbModel):
    user = One(User, on_delete=CASCADE, null=True, blank=True)
    name = CharField(max_length=200)
    email = EmailField(max_length=500, blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    id = UUIDField(default=id_type, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']


class ShoppingCart(DbModel):
    owner = One(Buyer, on_delete=CASCADE, null=True, blank=True)
    products = Many(Product)
    prise = IntegerField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    id = UUIDField(default=id_type, unique=True, primary_key=True, editable=False)
