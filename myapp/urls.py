from django.urls import path
from .views import home, category_products, products

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('category/<str:category>/', category_products, name='category_products'),
]
