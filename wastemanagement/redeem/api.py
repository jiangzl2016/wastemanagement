from redeem.models import Redeem
from rest_framework import viewsets, permissions
from .serializers import RedeemSerializer

# Redeem Viewset
class RedeemViewSet(viewsets.ModelViewSet):
    serializer_class = RedeemSerializer 
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_queryset(self):
        return self.request.user.redeem.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)