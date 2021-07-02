from django.urls import path
from ordersapp.views import OrderList, OrderCreate, OrderRead, OrderUpdate, OrderDelete
from ordersapp.views import forming_complete

app_name = "ordersapp"

urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('forming/complete/<pk>/', forming_complete, name='forming_complete'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('read/<pk>/', OrderRead.as_view(), name='read'),
    path('update/<pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<pk>/', OrderDelete.as_view(), name='delete'),
]
