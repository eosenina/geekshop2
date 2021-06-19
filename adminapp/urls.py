from django.urls import path

from adminapp.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView
from adminapp.views import CategoryListView, CategoryCreateView, CategoryUpdateView, admin_categories_remove
from adminapp.views import ProductListView, ProductCreateView, ProductUpdateView, admin_products_remove

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
    path('admin-categories-read/', CategoryListView.as_view(), name='admin_categories_read'),
    path('admin-categories-create/', CategoryCreateView.as_view(), name='admin_categories_create'),
    path('admin-categories-update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_categories_update'),
    path('admin-categories-remove/<int:category_id>/', admin_categories_remove, name='admin_categories_remove'),
    path('admin-products-read/', ProductListView.as_view(), name='admin_products_read'),
    path('admin-products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('admin-products-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('admin-products-remove/<int:product_id>/', admin_products_remove, name='admin_products_remove'),
]
