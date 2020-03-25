from rest_framework import serializers
from .models import Product, Order

# Serializers (to JSON)

# Para lista de produtos
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ['id', 'name', 'price', 'stock']

# Para os detalhes, alteração e criação de um produto.
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = '__all__' # Pega todos os fields

# Pedidos 
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields =  ['id','product','quantity','total_price', 'paid']

class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model  = Order
        fields =  ['id','product','quantity','total_price', 'paid']