from django.urls import path
from . import views
from rest_framework import routers
from shein.myapp.viewsets.ProductViewset import ProductViewSet


router = routers.DefaultRouter()

router.register('api/products', ProductViewSet, 'products')

router = routers.SimpleRouter()
router.register(r'Product', ProductViewSet, basename='Product')

urlpatterns = [
     path("", views.index, name="index"),
]
