from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'inventory', views.InventoryrViewSet, basename='MyInventory')
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'inventory', views.InventoryViewSet, basename='MyInventory')
urlpatterns = router.urls