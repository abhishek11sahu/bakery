from .models import *
from rest_framework import serializers
from accounts.serializers import OrderUserSerializer


class OrdersSerializer(serializers.ModelSerializer):
    user = OrderUserSerializer(many=False)

    class Meta:
        model = Orders
        fields = ['id', 'user', 'items', 'amount', 'created_at']
        depth = 1


class OrdersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
        depth = 0