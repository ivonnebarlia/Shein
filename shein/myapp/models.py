from django.db import models

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type_transaction = models.CharField(max_length=50)
    suppler = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Transaction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type_transaction = models.CharField(max_length=50)
    suppler = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('id',)
