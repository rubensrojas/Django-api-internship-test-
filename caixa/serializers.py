from rest_framework import serializers
from .models import Product

# Serializers (to JSON)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ['id', 'name', 'price', 'stock']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = '__all__' # Pega todos os fields
