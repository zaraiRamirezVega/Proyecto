from django.urls import path
from .views import home, category_products, products

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('category/<str:category>/', views.category_products, name='category_products'),
    path('logout/', views.logout, name='logout'),
]
