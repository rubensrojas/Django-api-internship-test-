from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# API 
from .models import Product, Order
from .serializers import ProductSerializer, ProductDetailSerializer, OrderSerializer, OrderDetailSerializer

# Create your views here.


#### Products View ####

class ProductsListCreateAPIView(APIView):
    """ GET - Lista todos os Produtos &
        POST - Cria um produto """
    # Autenticação
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # GET - Listando todos os produtos 
    def get(self, request):
        products = Product.objects.all()
        serilalizer = ProductSerializer(products, many=True)
        return Response(serilalizer.data)
    
    # POST - Criando um produto
    def post(self, request):
        # Criando
        serializer = ProductDetailSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ GET - PATCH - DELETE - Em um produto especifico  """
    # Autenticação
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Queryset
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'



#### Orders View ####

class OrderListCreateAPIView(APIView):
    """ GET - Lista todos os pedidos do usuário """
    # Autenticação
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET - Listando todos os produtos 
    def get(self, request):
        # Informações do usuário
        user = request.user
        username = user.username
        # Pegando informações
        orders = Order.objects.filter(owner__username=username)
        serializer = OrderDetailSerializer(orders, many=True)
        return Response(serializer.data)

    """ Expect:
    { 
    "product": 2,       # Sendo este número o id do produto
    "quantity": 10
    }"""
    def post(self, request):
        # Informações do usuário
        username = request.user.username
        # Dados
        data        = request.data
        # Separando Dados
        product_id   = request.data.get("product", )
        quantity     = request.data.get("quantity", )
        product      = Product.objects.get(id=product_id)
        productstock = product.stock

        # Caso não houver estoque suficiente
        if quantity > productstock:
            resposta = 'Estoque inferior á quantidade requisita. Estoque: ' + str(productstock)
            return Response(resposta, status = status.HTTP_400_BAD_REQUEST)

        # Concatenando os dados
        price       = product.price
        total_price = quantity * price
        data['total_price'] = total_price

        # Dados
        #data = get_dados(request)
        serializer = OrderSerializer(data = data)
        
        if serializer.is_valid():
            product.stock -= quantity  # Atualizando o estoque
            product.save()
            serializer.save(owner=request.user) # Salvando e definindo usuário
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OrderRetriveUpdateDeleteAPIView(APIView):
    # Autenticação
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        username = request.user.username
        try:
            queryset = Order.objects.filter(owner__username=username)
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

    # expect JSON { "quantity": 10 } Exemplo
    def patch(self, request, id):
        username = request.user.username
        try:
            queryset = Order.objects.filter(owner__username=username)
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        quantity   = request.data.get("quantity", )
        # Se a quantidade == quantidade nova, então apenas retorne
        if order.quantity == quantity:
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Logica: soma a quantidade do pedido com o estoque para ter o valor do estoque inicial antes deste pedido.
        productstock = order.product.stock + order.quantity

        # Caso não houver estoque suficiente
        if quantity > productstock:
            resposta = 'Estoque inferior á quantidade requisita. Quantidade máxima: ' + str(productstock)
            return Response(resposta, status = status.HTTP_400_BAD_REQUEST)
        elif quantity < 0:
            resposta = 'Quantidade negativa. Quantidade máxima: ' + str(productstock)
            return Response(resposta, status = status.HTTP_400_BAD_REQUEST)

        # Atualizando preço e estoque
        product_id = order.product.id
        product = Product.objects.get(id=product_id)
        product.stock = productstock - quantity
        total_price = product.price * quantity

        # Salvando alterações
        product.save()
        order.quantity = quantity
        order.total_price = total_price
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        username = request.user.username
        try:
            queryset = Order.objects.filter(owner__username=username)
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Adicionando ao estoque
        product_id     = order.product.id
        product        = Product.objects.get(id=product_id)
        product.stock += order.quantity
        product.save()

        # Deletando
        order.delete()
        resposta = "Deletado com sucesso."
        return Response(resposta, status = status.HTTP_204_NO_CONTENT)


class OrderPayAPIView(APIView):
    # Autenticação
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        username = request.user.username
        try:
            queryset = Order.objects.filter(owner__username=username)
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        order.paid = True
        order.save()
        serializer = OrderDetailSerializer(order)

        return Response(serializer.data)


