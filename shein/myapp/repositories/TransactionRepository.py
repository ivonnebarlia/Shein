from myapp.models import Transaction


class TransactionRepository:

    def get_all_products(self):
        return Transaction.objects.all()