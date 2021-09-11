from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.product_delete,
         name='dashboard-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail,
         name='dashboard-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit,
         name='dashboard-products-edit'),
    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='dashboard-customer-detail'),
    path('order/', views.order, name='dashboard-order'),
    path('order/delete/<int:pk>/', views.order_delete,
         name='dashboard-order-delete'),
    path('order/detail/<int:pk>/', views.order_detail,
         name='dashboard-order-detail'),
    path('order/edit/<int:pk>/', views.order_edit,
         name='dashboard-order-edit'),
]
