from django.db import models
from registro.models import User

class publicacao(models.Model):
    user1= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.TextField(max_length=500)
    
    def __str__(self):
        return self.post
    