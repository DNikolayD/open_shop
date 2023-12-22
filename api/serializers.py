from rest_framework.serializers import ModelSerializer
from products.models import Tag, Product, Image, Review, Business
from users.models import Seller, Buyer, ShoppingCart
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BuyerSerializer(ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    sender = BuyerSerializer(many=False)

    class Meta:
        model = Review
        fields = '__all__'


class SellerSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Seller
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ShoppingCartSerializer(ModelSerializer):
    owner = BuyerSerializer(many=False)
    products = ProductSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class BusinessSerializer(ModelSerializer):
    owner = SellerSerializer(many=False)
    products = ProductSerializer(many=True)

    class Meta:
        model = Business
        fields = '__all__'
