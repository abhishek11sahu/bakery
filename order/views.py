from django.shortcuts import render
from .serializers import *
from inventory.serializers import MenuSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ViewMenuList(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class OrdersList(RetrieveAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'

    def get_queryset(self):
        print(dir(self.request))
        print(self.request.query_params)
        if self.request.query_params and 'user' in self.request.query_params:
            queryset = Orders.objects.filter(user_id=self.request.query_params['user'])
        else:
            queryset = Orders.objects.all()
            print(queryset.values())

        return queryset


class OrdersCreate(CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersCreateSerializer
    permission_classes = [IsAuthenticated]


class OrderDetail(RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]
