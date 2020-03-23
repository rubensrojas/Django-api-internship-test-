from rest_framework import serializers
from .models import Products, Users, Orders

# Serializers (to JSON)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Products
        fields = ['id', 'name', 'price', 'stock']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Products
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Orders
        fields = ['id', 'product', 'quantity', 'total_price','paid']