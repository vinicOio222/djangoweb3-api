from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet

router = DefaultRouter()
router.register('', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

