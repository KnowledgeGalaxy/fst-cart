from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView
from .views import CategoryListCreateAPIView,CategoryDetailAPIView
from .views import CustomerListCreateView, CustomerDetailView
from .views import AddressList, AddressDetail
from .views import LoginAPIView
from .views import  OrderedItemsAPIView, ConfirmOrderAPIView, BillAPIView, OrderedItemsDetailAPIView, AddressDetailById, ConfirmOrderDetailAPIView
urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<str:customer_id>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<str:customer_id>/addresses/', AddressList.as_view(), name='address-list'),
    path('customers/<str:customer_id>/addresses/<int:address_id>/', AddressDetail.as_view(), name='address-detail'),
    path('addresses/<int:address_id>/', AddressDetailById.as_view(), name='address-detail-by-id'),
    path('ordered-items/', OrderedItemsAPIView.as_view(), name='ordered-items'),
    path('ordered-items/<int:item_id>/', OrderedItemsDetailAPIView.as_view(), name='ordered-item-detail'),
    path('confirm-orders/', ConfirmOrderAPIView.as_view(), name='confirm-orders'),
    path('confirm-orders/<int:id>/', ConfirmOrderDetailAPIView.as_view(), name='confirm-order-detail'),
    path('create-bill/', BillAPIView.as_view(), name='create-bill'),
]



