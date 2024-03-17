from django.urls import path
from . import views
from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()

router.register('api/products', ProductViewSet, 'products')

urlpatterns = [
     path("", views.index, name="index"),
]
