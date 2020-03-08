from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Redeem(models.Model):
    phone = models.CharField(max_length=100)
    bag_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="redeem", on_delete=models.CASCADE, null=True)
