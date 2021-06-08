from .models import *
from rest_framework import serializers


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    #ingredients = IngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        #fields = ['dish_name', 'ingredients', 'cost_price', 'selling_price', 'created_at', 'updated_at']
        fields = "__all__"
        depth = 1


class MenuCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"
        depth = 0