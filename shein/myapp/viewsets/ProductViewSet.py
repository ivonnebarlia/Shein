from rest_framework import viewsets, permissions

from myapp.repositories.productRepository import ProductRepository
from myapp.serializers.ProductSerializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductRepository.get_all_products()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer