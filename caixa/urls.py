from django.urls import path, include
from .views import ( 
    ProductsListCreateAPIView,
    ProductsRetrieveUpdateDestroyAPIView
    )
from account.views import AccountRegistrationView
# Token
from rest_framework.authtoken.views import obtain_auth_token

# Urls

urlpatterns = [
    path('products', ProductsListCreateAPIView.as_view(), name = 'product-list'),                        # GET - Lista todos os produtos
    path('products/<int:id>', ProductsRetrieveUpdateDestroyAPIView.as_view(), name = 'product-detail'),  # GET - Pega um produto especifico
    path('account/registration', AccountRegistrationView.as_view(), name = 'registration'),              # POST - Registra o usuário
    path('account/login', obtain_auth_token, name = 'login'),                                            # POST - Faz login de um usuário e recupera seu Token
    ]