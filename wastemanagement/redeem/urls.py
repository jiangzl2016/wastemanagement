from rest_framework import routers
from .api import RedeemViewSet

router = routers.DefaultRouter()
router.register('api/redeem', RedeemViewSet, 'redeem')

urlpatterns = router.urls