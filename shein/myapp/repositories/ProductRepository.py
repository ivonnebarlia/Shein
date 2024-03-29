from myapp.models import Product


class ProductRepository:

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(id):
        return Product.objects.get(id=id)