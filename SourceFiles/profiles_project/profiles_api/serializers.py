# creating a serializer object to help convert between JSON and python objects
# it's best practice to keep all the serializers in this file
from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    # serializes a name field to test an APIView

    name = serializers.CharField(max_length=20)
