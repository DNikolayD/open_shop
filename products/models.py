from django.db.models import (Model as DbModel, UUIDField as IdField, TextField, CharField as SmallTextField,
                              ManyToManyField as Many, ImageField, FloatField, SmallIntegerField, DateTimeField,
                              ForeignKey as One, CASCADE)
from uuid import uuid4 as id_type

from users.models import Seller, Buyer
# Create your models here.


class Image(DbModel):
    id = IdField(default=id_type, unique=True, primary_key=True, editable=False)
    created = DateTimeField(auto_now_add=True)
    image = ImageField()


class Tag(DbModel):
    id = IdField(default=id_type, unique=True, primary_key=True, editable=False)
    created = DateTimeField(auto_now_add=True)
    name = SmallTextField(max_length=200)


class Product(DbModel):
    id = IdField(default=id_type, unique=True, primary_key=True, editable=False)
    created = DateTimeField(auto_now_add=True)
    name = SmallTextField(max_length=200)
    description = TextField()
    images = Many(to=Image, null=True, blank=True)
    tags = Many(to=Tag, null=True, blank=True)
    prise = FloatField(max_length=10000)


class Business(DbModel):
    id = IdField(default=id_type, unique=True, primary_key=True, editable=False)
    created = DateTimeField(auto_now_add=True)
    owner = One(to=Seller, null=True, blank=True, on_delete=CASCADE)
    name = SmallTextField(max_length=200)
    products = Many(to=Product, null=True, blank=True)


class Review(DbModel):
    id = IdField(default=id_type, unique=True, primary_key=True, editable=False)
    sender = One(to=Buyer, null=True, blank=True, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
    content = TextField()
    rating = SmallIntegerField(max_length=5)
