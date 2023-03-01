from django.db import models
from user.models import User

class Bicycle(models.Model):
    nickname   = models.CharField(max_length=10)
    modelname  = models.CharField(max_length=20)
    year       = models.PositiveIntegerField()
    type       = models.CharField(max_length=10)
    user       = models.ForeignKey("user.User", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'bicycles'

    def __str__(self):
        return self.nickname