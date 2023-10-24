from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView
from .views import CategoryListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),

]