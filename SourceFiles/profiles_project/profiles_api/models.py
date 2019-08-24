# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    # Helps django work with our custom base user model
    def createUser(self, email, name, password=None):
        # creates a suer that matches our model
        if not email:
            raise ValueError("Please provide an email address")

        # The normalize_email function is there only to ensure that all emails in our system are standardized
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # The set_password function creates a hash value for the password given and stores it in our database
        user.set_password(password)

        # This line saves the user to our database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name):
        # creates a super user who is basically someone who can access anything on the server
        user = self.createUser(email=email, password=password, name=name)

        user.isSuperUser = True

        user.save(using=self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Represents a user profile inside this system
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    # The below is an object manager
    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def getFullName(self):
        # This function returns a user's full name
        return self.name

    def getShortName(self):
        # This function returns a short name for the user
        return self.name

    def __str__(self):
        # Django uses this to convert the object into a nice readable form
        return self.email
