from django.db import models
from django.contrib.auth.models import AbstractUser
from preferences.models import Preference

class UserProfile(AbstractUser):
    birth_date = models.DateField(default= "1993-07-19")
    phone = models.CharField(max_length=15)
    preferences = models.ManyToManyField(Preference, blank=True)

    # Define `related_name` para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        blank=True,
    )

    def __str__(self):
        return self.username
