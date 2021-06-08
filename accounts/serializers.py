from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'date_joined')
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }
