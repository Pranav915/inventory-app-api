from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

class Club(models.Model):
    """Database model for clubs in the system"""
    club_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        """Return String Representation of user"""
        return self.email



