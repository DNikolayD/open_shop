from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProductSerializer, BusinessSerializer, UserSerializer, SellerSerializer, BuyerSerializer, \
    ShoppingCartSerializer
from products.models import Product, Business, Review
from users.models import ShoppingCart, Buyer
from .permisions import IsSeller, IsBuyer


@api_view(['GET'])
def get_routes(request):

    routes = [
        # tested
        {'GET': '/api/products'},
        {'GET': '/api/products/id'},
        {'POST': '/api/products/id/review'},
        {'POST': '/api/products-create'},
        {'PUT': '/api/products/update/id'},
        {'DELETE': '/api/products/delete/id'},

        # not tested
        {'GET': '/api/businesses'},
        {'GET': '/api/businesses/id'},
        {'POST': '/api/businesses-create'},
        {'PUT': '/api/businesses/update/id'},
        {'DELETE': '/api/businesses/delete/id'},

        {'GET': '/api/sellers'},
        {'POST': '/api/sellers/create'},
        {'PUT': '/api/seller/update'},
        {'DELETE': '/api/seller/delete'},

        {'GET': '/api/buyers'},
        {'POST': '/api/buyers/create'},
        {'PUT': '/api/buyer/update'},
        {'DELETE': '/api/buyer/delete'},

        {'GET': '/api/shopping-carts'},
        {'POST': '/api/shipping-carts/create'},
        {'PUT': '/api/shipping-carts/update'},
        {'DELETE': '/api/shipping-carts/delete'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'}
    ]
    return Response(routes)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsBuyer])
def product_review(request, pk):
    product = Product.objects.get(id=pk)
    sender = request.user.buyer
    data = request.data
    business = None
    for item in Business.objects.all():
         if item.products.get(id=pk) is not None:
             business = item
             break
    owner = business.owner

    review, created = Review.objects.get_or_create(
        sender=sender,
        rating=data['rating'],
        content=data['content']
    )
    review.save()
    owner.reviews.add(review)
    owner.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsSeller])
def create_product(request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=HTTP_201_CREATED)
    else:
        print('error', product_serializer.errors)
        return Response(product_serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsSeller])
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product = product_serializer.save()
        return Response(product_serializer.data)
    else:
        print('error', product_serializer.errors)
        return Response(product_serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsSeller])
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response()


@api_view(['GET'])
def get_businesses(request):
    businesses = Business.objects.all()
    serializer = BusinessSerializer(businesses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_business(request, pk):
    business = Business.objects.get(id=pk)
    serializer = BusinessSerializer(business, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsSeller])
def create_business(request):
    serializer = BusinessSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsSeller])
def update_business(request, pk):
    business = Business.objects.get(id=pk)
    serializer = BusinessSerializer(data=request.data)
    if serializer.is_valid():
        business = serializer.save()
        return Response(serializer.data)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsSeller])
def delete_business(request, pk):
    business = Business.objects.get(id=pk)
    business.delete()
    return Response()


@api_view(['GET'])
@permission_classes([IsSeller])
def get_seller(request):
    seller = request.user.seller
    serializer = SellerSerializer(seller, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_seller(request):
    serializer = SellerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsSeller])
def update_seller(request):
    seller = request.user.seller
    serializer = SellerSerializer(data=request.data)
    if serializer.is_valid():
        seller = serializer.save()
        return Response(serializer.data)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsSeller])
def delete_seller(request):
    seller = request.user.seller
    seller.delete()
    return Response()


@api_view(['GET'])
@permission_classes([IsBuyer])
def get_buyer(request):
    buyer = request.user.buyer
    serializer = BuyerSerializer(buyer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_buyer(request):
    data = request.data
    data["name"] = data["user"]["username"]
    user=UserSerializer(data=data["user"])
    if user.is_valid():
        user.save()
    else:
        print('error', user.errors)
        return Response(user.errors, status=HTTP_400_BAD_REQUEST)
    serializer = BuyerSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsBuyer])
def update_buyer(request):
    buyer = request.user.buyer
    data = request.data
    data["name"] = data["user"]["username"]
    serializer = BuyerSerializer(data=data)
    if serializer.is_valid():
        buyer = serializer.save()
        return Response(serializer.data)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsBuyer])
def delete_buyer(request):
    buyer = request.user.buyer
    buyer.delete()
    return Response()


@api_view(['GET'])
@permission_classes([IsBuyer])
def get_shopping_cart(request):
    buyer = request.user.buyer
    shopping_cart = ShoppingCart.objects.get(owner=buyer)
    serializer = ShoppingCartSerializer(shopping_cart, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsBuyer])
def create_shopping_cart(request):
    serializer = ShoppingCartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsBuyer])
def update_shopping_cart(request):
    buyer = request.user.buyer
    shopping_cart = ShoppingCart.objects.get(owner=buyer)
    serializer = ShoppingCartSerializer(data=request.data)
    if serializer.is_valid():
        shopping_cart = serializer.save()
        return Response(serializer.data)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsBuyer])
def delete_shopping_cart(request):
    buyer = request.user.buyer
    shopping_cart = ShoppingCart.objects.get(owner=buyer)
    shopping_cart.delete()
    return Response()
