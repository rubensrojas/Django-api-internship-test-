from django.urls import path, include
from .views import ( 
    ProductsListAPIview, ProductsCreateAPIView,
    ProductsRetrieveUpdateDestroyAPIView
    )

# Urls

urlpatterns = [
    path('products/', ProductsListAPIview.as_view(), name = 'product-list'),                              # GET - Lista todos os produtos
    path('products/create', ProductsCreateAPIView.as_view(), name = 'product-create'),                    # POST - Cria um produto
    path('products/<int:id>/', ProductsRetrieveUpdateDestroyAPIView.as_view(), name = 'product-detail'),  # GET - Pega um produto especifico
    #path('products/<int:id>/edit/', ProductsUpdateAPIView.as_view(),   name = 'product-edit'),    # PATCH - Edita um produto
    #path('products/<int:id>/delete/', ProductsDeleteAPIView.as_view(), name = 'product-edit'),    # DELETE - Deleta um produto
]