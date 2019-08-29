# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# this is basically the logic behind our application
class HelloAPIView(APIView):
    # testing APIView

    def get(self, request, format=None):
        # returns a list of API Features
        an_apiview = [
            'Uses HTTP functions as functions',
            'Similar to a traditional Django View',
            'Gives the most control over the application logic',
            'Mapped manually to URLS'
        ]

        return Response({'message': 'Hello', ', APIView': an_apiview})
