from shein.myapp.models import Product, Transaction
from rest_framework import viewsets, permissions
from shein.myapp.serializers import ProductSerializer
from shein.myapp.repositories import ProductRepository


class ProductViewSet(viewsets.modelViewSet):
    queryset = ProductRepository.get_all_products()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
