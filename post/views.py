from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from registro.models import User


class publiApi(generics.ListCreateAPIView):
   # permission_classes=(IsAuthenticated, )
    queryset= models.publicacao.objects.all()
    serializer_class= serializers.publiSerializers
    
class publiView(generics.RetrieveUpdateDestroyAPIView):
   #  permission_classes=(IsAuthenticated, )
    queryset= models.publicacao.objects.all()
    serializer_class= serializers.publiSerializers
    