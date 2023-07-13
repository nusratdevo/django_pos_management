
from django.urls import path
# from main.views.dashboard_view import Dashboard
from main.views.auth_view import UserLoginView, LogoutView, Dashboard
from main.views import category_view, product_view, pos_view
from main.views.subcat_view import SubCategoryCreateView, SubCategoryListView, SubCategoryUpdateView, SubCategoryDeleteView

from main.views.product_view import (
    ProductList, ProductCreate, ProductUpdate,
    delete_image, delete_variant
)
# from customers import pdfviews,billviews





urlpatterns = [
    path('', UserLoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),

   ## Category Url
    path('category/',category_view.category_list, name='category_list'),
    path('category/create/', category_view.category_form,name='category_create'), 
    path('category/update/<int:id>/', category_view.category_form,name='category_update'), 
    path('category/delete/<int:id>/',category_view.employee_delete,name='category_delete'),

   ## Sub category url
    path('subcategory/', SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<pk>/', SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory-delete/<pk>/', SubCategoryDeleteView.as_view(), name='subcategory_delete'),
# ## Sub category url
#     path('customer/', CustomerCreateView.as_view(), name='customer_create'),
#     path('customer/<pk>/', CustomerUpdateView.as_view(), name='customer_update'),
#     path('customer-delete/<pk>/', CustomerDeleteView.as_view(), name='customer_delete'),


# Product Url
# path('product/',product_view.product_list, name='product_list'),
path('stock/',product_view.product_stock, name='product_stock'),
# path('product/create/',product_view.product_form, name='product_create'),
path('products/', ProductList.as_view(), name='list_products'),
path('create/', ProductCreate.as_view(), name='create_product'),
path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
path('delete-image/<int:pk>/', delete_image, name='delete_image'),
path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
path('stock/update/<int:id>/', product_view.update_qty, name='update_qty'),
path('attrbute/update/', product_view.edit_qty, name='edit_attr'),



# POS Url

path('pos/create/',pos_view.pos_create, name='pos_create'),
path('checkout-modal', pos_view.checkout_modal, name="checkout-modal"),
path('save-pos', pos_view.save_pos, name="save-pos"),
path('receipt', pos_view.receipt, name="receipt-modal"),
path('order/', pos_view.order_list, name="order-list"),
path('order/status/<int:id>/', pos_view.order_status, name="status_change"),
path('order/traking/<int:id>/', pos_view.order_traking, name="traking"),

path('order/delete/<int:id>/', pos_view.delete_order, name="delete-order"),
path('order/invoice', pos_view.order_invoice, name="order-invoice"),

# path('orders/bill/<int:cid>',billviews.GenerateBILL.as_view(),name="bill"),




]