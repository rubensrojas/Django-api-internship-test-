#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
#from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
#from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer, ProductDetailSerializer

# Create your views here.


#### Products View ####

class ProductsListAPIview(ListAPIView):
    """ GET - Lista todos os Produtos """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductsCreateAPIView(CreateAPIView):
    """ POST - Cria um produto """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ GET - PATCH - DELETE - Em um produto especifico  """
    queryset = Products.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'

#### Orders View ####


#### User view ####

