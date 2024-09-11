
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True, null=True)
    preferences = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

