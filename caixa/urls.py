from django.urls import path, include
from .views import Products

# Urls

urlpatterns = [
    path('products/', Products.as_view())
]