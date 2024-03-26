from shein.myapp.models import Product, Transaction
from rest_framework import viewsets, permissions
from shein.myapp.serializers import TransactionSerializer
from shein.myapp.repositories import TransactionRepository


class TransactionViewSet(viewsets.modelViewSet):
    queryset = TransactionRepository.get_all_products()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TransactionSerializer