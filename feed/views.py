from django.shortcuts import render
from . import serializers
from .models import Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from post.models import *

class postView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class=serializers.PostSerializer
    #permission_classes= (IsAuthenticated, )
    
    def get_queryset(self):
            # Implemente a lógica para obter as postagens do feed
        queryset = publicacao.objects.filter().order_by('-id')
        return queryset