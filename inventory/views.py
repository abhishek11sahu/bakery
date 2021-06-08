from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class IngredientsList(ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class IngredientsUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class MenuList(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class MenuCreate(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class MenuUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
