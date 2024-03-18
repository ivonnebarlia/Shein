from .models import Product, Transaction
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, TransactionSerializer


class ProductViewSet(viewsets.modelViewSet):
    queryset = Product.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer


class TransactionViewSet(viewsets.modelViewSet):
    queryset = Transaction.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TransactionSerializer