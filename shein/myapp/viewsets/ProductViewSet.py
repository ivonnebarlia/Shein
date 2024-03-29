from rest_framework import viewsets, permissions
from myapp.serializers import ProductSerializer
from myapp.repositories.ProductRepository import ProductRepository


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductRepository.get_all_products()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
