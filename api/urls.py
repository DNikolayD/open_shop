from django.urls import path
from .views import (get_routes,
                    get_products, get_product, product_review, create_product, update_product, delete_product,
                    get_businesses, get_business, create_business, update_business, delete_business,
                    get_seller, create_seller, update_seller, delete_seller,
                    get_buyer, create_buyer, update_buyer, delete_buyer,
                    get_shopping_cart, create_shopping_cart, update_shopping_cart, delete_shopping_cart)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', get_routes),
    path('products', get_products),
    path('products/<str:pk>', get_product),
    path('products/<str:pk>/review', product_review),
    path('products-create', create_product),
    path('products/update/<str:pk>', update_product),
    path('products/delete/<str:pk>', delete_product),
    path('businesses', get_businesses),
    path('businesses/<str:pk>', get_business),
    path('businesses-create', create_business),
    path('businesses/update/<str:pk>', update_business),
    path('businesses/delete/<str:pk>', delete_business),
    path('sellers/', get_seller),
    path('sellers/create', create_seller),
    path('sellers/update', update_seller),
    path('sellers/delete', delete_seller),
    path('buyers', get_buyer),
    path('buyers/create', create_buyer),
    path('buyers/update', update_buyer),
    path('buyers/delete', delete_buyer),
    path('shipping-carts', get_shopping_cart),
    path('shipping-carts/create', create_shopping_cart),
    path('shipping-carts/update', update_shopping_cart),
    path('shipping-carts/delete', delete_shopping_cart),
]
