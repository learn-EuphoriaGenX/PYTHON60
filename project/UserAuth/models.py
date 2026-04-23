from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class OtpModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class PremiumUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username