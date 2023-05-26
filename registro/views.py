from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import generics

class UserApi(generics.ListCreateAPIView):
    queryset=models.User.objects.all()
    serializer_class=serializers.UserSerializer
    
class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.User.objects.all()
    serializer_class=serializers.UserSerializer
    