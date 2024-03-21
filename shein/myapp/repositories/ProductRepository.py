from shein.myapp.models import Product


class ProductRepository:

    def get_all_products(self):
        return Product.objects.all()