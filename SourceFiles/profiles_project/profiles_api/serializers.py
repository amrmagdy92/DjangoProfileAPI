# creating a serializer object to help convert between JSON and python objects
# it's best practice to keep all the serializers in this file
from rest_framework import serializers
from . import models

class HelloSerializers(serializers.Serializer):
    # serializes a name field to test an APIView

    name = serializers.CharField(max_length=20)

class UserProfileSerializer(serializers.ModelSerializer):
    # A serializer for our user profile object
    # metadata for our user
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # creates and returns a new user
    def create(self, validated_data):
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    # A serializer for feed items
    class Meta:
        model = models.ProfileFeedItem
        fields = ('ID', 'user_profile', 'status_text', 'creation_date')
        extra_kwargs = {'user_profile': {'read_only': True}}