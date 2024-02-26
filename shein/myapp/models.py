from django.db import models

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    purchase_date = models.DateField()
    initial_inventory = models.IntegerField()
    quantity = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    received_quantity = models.PositiveIntegerField()
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
