from django.db import models
from post.models import publicacao

class Post(models.Model):
    name= models.CharField(max_length=255)
    user2= models.ForeignKey(publicacao, on_delete=models.CASCADE, related_name='post_related')