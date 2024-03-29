from django.urls import path, include
from . import views
# from rest_framework import routers
# from myapp.viewsets import ProductViewSet

# router = routers.SimpleRouter()

# router.register(r'Product', ProductViewSet, basename='Product')

urlpatterns = [
     path("", views.index, name="index"),
     # path('', include(router.urls)),
]
