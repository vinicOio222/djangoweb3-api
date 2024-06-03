from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from blockchain.api.views import TransactionViewSet

router = DefaultRouter()

router.register('transactions', TransactionViewSet, basename="transactions")



permissions_classes = [AllowAny]
app_name = "api_root"
urlpatterns = router.urls