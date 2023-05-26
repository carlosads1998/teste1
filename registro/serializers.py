from . import models
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields= ('__all__')
        extra_kwargs={
            'password': {'write_only':True}
            }

