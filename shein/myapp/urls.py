from django.urls import path, include
from . import views
from rest_framework import routers
from myapp.viewsets import ProductViewSet
from rest_framework.routers import DefaultRouter
from .viewsets.TransactionViewset import TransactionViewSet

router = DefaultRouter()

# router.register(r'products', ProductViewSet, basename='product')
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
     path('', include(router.urls)),
]
