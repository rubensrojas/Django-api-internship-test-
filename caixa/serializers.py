from rest_framework import serializers
from .models import Product, User, Order

# Serializers (to JSON)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = '__all__'
        #fields = ['id', 'name', 'description', 'price', 'stock']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields = ['id', 'product', 'quantity', 'total_price','paid']