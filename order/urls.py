from django.urls import path
from .views import OrdersList, OrdersCreate, OrderDetail, ViewMenuList

urlpatterns = [
    path("menu_list/", ViewMenuList.as_view()),
    path("orders_list/<int:user>", OrdersList.as_view()),
    path("orders_create/", OrdersCreate .as_view()),
    path("order_detail/<int:pk>", OrderDetail.as_view()),
]
