from django.urls import path, include
from .views import ( 
    ProductsListCreateAPIView,
    ProductsRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView,
    OrderRetriveUpdateDeleteAPIView,
    OrderPayAPIView
    )
from account.views import AccountRegistrationView

# Token
from rest_framework.authtoken.views import obtain_auth_token

# Urls

urlpatterns = [
    #products
    path('products', ProductsListCreateAPIView.as_view(), name = 'product-list-create'),                          # GET - Lista todos os produtos
    path('products/<int:id>', ProductsRetrieveUpdateDestroyAPIView.as_view(), name = 'product-detail'),           # GET - PATCH - DELETE - De um produto especifico
    #orders
    path('orders', OrderListCreateAPIView.as_view(), name = 'orders-list-create'),                                # GET - POST - Lista todos os pedidos do usuário / Cria um pedido
    path('orders/<int:id>', OrderRetriveUpdateDeleteAPIView.as_view(), name = 'orders-detail-update-delete'),     # GET - PATCH - DELETE - Pega, atualiza ou deleta um pedido em especifico
    path('orders/<int:id>/pay', OrderPayAPIView.as_view(), name = 'orders-pay'),                                  # POST - Paga o pedido: "paid" = True
    #account
    path('account/registration', AccountRegistrationView.as_view(), name = 'registration'),                       # POST - Registra o usuário
    path('account/login', obtain_auth_token, name = 'login'),                                                     # POST - Faz login de um usuário e recupera seu Token
    ]