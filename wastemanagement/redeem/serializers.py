from rest_framework import serializers
from redeem.models import Redeem

class RedeemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redeem
        fields = '__all__'