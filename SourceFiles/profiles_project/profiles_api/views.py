# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions

# Create your views here.
# this is basically the logic behind our application
class HelloAPIView(APIView):
    # testing APIView

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        # returns a list of API Features
        # this is typically where some of the app logic goes
        an_apiview = [
            'Uses HTTP functions as functions',
            'Similar to a traditional Django View',
            'Gives the most control over the application logic',
            'Mapped manually to URLS'
        ]

        return Response({'message': 'Hello', ', APIView': an_apiview})

    def post(self, request):
        # create a hello message with a name posted to the API
        serializer = serializers.HelloSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello, {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # Handles updating an object
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        # Handles partial update of an object
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        # Handles deletion of an object
        return Response({'method': 'delete'})

class HelloViewSets(viewsets.ViewSet):
    # Testing viewsets

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        # returns a hello message
        a_viewset = [
        'Uses actions list, create, retrieve, update, partial_update methods',
        'Automatically routes to URLs using routers',
        'Provide more functionality with less code'
        ]

        return Response({'message': 'Hello', ',ViewSet': a_viewset})

    def create(self, request):
        # handles the creation of a new object in our database
        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello, {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Handles the retrieval of an object with its ID
        return Response({'This corresponds to http method': 'GET'})

    def update(self, request, pk=None):
        # Handles the update of an object in the database
        return Response({'This corresponds to http method': 'PUT'})

    def partial_update(self, request, pk=None):
        # handles the partial update of an object in the database
        return Response({'This corresponds to http method': 'PATCH'})

    def destory(self, request, pk=None):
        # handles the deletion of an object from the database
        return Response({'This corresponds to http method': 'DELETE'})

# This class is for the profiles APIs
class UserProfileViewSet(viewsets.ModelViewSet):
    # our serializer
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
