# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUSer
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UserProfile(AbstractBaseUSer, PermissionsMixin):
    """Represents a user profile inside this system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    isStaff = models.BooleanField(default=False)

    """The below is an object manager"""
    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def getFullName(self):
        """This function returns a user's full name"""
        return self.name

    def getShortName(self):
        """This function returns a short name for the user"""
        shortName = f"{self.firstName} {self.lastName}"
        return shortName

    def __str__(self):
        """Django uses this to convert the object into a nice readable form"""
        return self.email
