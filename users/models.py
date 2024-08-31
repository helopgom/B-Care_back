from django.db import models
from django.contrib.auth.models import User
#from preferences.models import Preference

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    #preferences = models.ManyToManyField(Preference, blank=True)

    def __str__(self):
        return self.user.username
