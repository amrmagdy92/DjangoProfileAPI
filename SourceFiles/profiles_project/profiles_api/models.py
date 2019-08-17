# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUSer
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfile(AbstractBaseUSer, PermissionsMixin):
    #Represents a user profile inside this system

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    isStaff = models.BooleanField(default=False)

    #The below is an object manager
    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def getFullName(self):
        #This function returns a user's full name
        return self.name

    def getShortName(self):
        #This function returns a short name for the user
        shortName = f"{self.firstName} {self.lastName}"
        return shortName

    def __str__(self):
        #Django uses this to convert the object into a nice readable form
        return self.email

class UserProfileManager(BaseUserManager):
    #Helps django work with our custom base user model
    def createUser(self, email, password=none, name, firstName, lastName):
        # creates a suer that matches our model
        if not email:
            raise ValueError("Please provide an email address")

        # The normalize_email function is there only to ensure that all emails in our system are standardized
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, firstName=firstName, lastName=lastName)

        # The set_password function creates a hash value for the password given and stores it in our database
        user.set_password(password)

        # This line saves the user to our database
        user.save(using=self._db)

        return user

    def createSuperUser(self, email, password, name, firstName, lastName):
        # creates a super user who is basically someone who can access anything on the server
        user = self.createUser(email=email, password=password, name=lastName, firstName=firstName,lastName=lastName)

        user.isSuperUser = True
        user.isStaff = True

        user.save(using=self._db)
