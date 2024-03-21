from rest_framework import serializers
from shein.myapp.models import Transaction, Product
from shein.myapp.serializers import ProductSerializer


class TransactionSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(read_only=True)
    class Meta:
        model_transaction = Transaction
        fields = ('id', 'product_id', 'amount', 'price', 'date', 'type_transaction', 'suppler ')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance