from rest_framework import viewsets, permissions
from myapp.models import Transaction
from myapp.serializers.TransactionSerializer import TransactionReadSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TransactionReadSerializer
