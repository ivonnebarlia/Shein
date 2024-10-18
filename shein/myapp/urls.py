from django.urls import path, include
from myapp.viewsets import ProductViewSet
from rest_framework.routers import DefaultRouter
from .viewsets.TransactionViewset import TransactionViewSet

router = DefaultRouter()
router.register('api/products', ProductViewSet, 'products')
router.register(r'transactions', TransactionViewSet, basename='transactions')
# urlpatterns = [
#      path("", views.index, name="index"),
urlpatterns = [
     path('', include(router.urls)),
]
