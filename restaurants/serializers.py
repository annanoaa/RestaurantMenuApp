from rest_framework import serializers
from .models import Restaurant, MainCategory, SubCategory, Dish, Ingredient

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')

class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number', 'cover_image')

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ('id', 'name')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')

class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'image', 'price', 'ingredients')

class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'cover_image')

class SubCategoryDetailSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'cover_image', 'dishes')