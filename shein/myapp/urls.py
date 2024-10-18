from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.viewsets.productViewSet import ProductViewSet
from myapp.viewsets.transactionViewSet import TransactionViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, 'products')
router.register(r'transactions', TransactionViewSet, basename='transactions')
urlpatterns = [
     path('', include(router.urls)),
]
