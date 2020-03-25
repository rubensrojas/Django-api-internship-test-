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
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

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
#   user = request.user
#   if order.owner != user: raise error

#### User view ####

