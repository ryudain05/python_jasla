import email
from unicodedata import name
from django.db import models
from django.core.validators import RegexValidator # 전화번호 벨리데이션

class User(models.Model):
    name             = models.CharField(max_length=10)
    nickname         = models.CharField(max_length=10,unique=True)
    email            = models.EmailField(max_length=100,unique=True)
    password         = models.CharField(max_length=256)
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone            = models.CharField(validators = [phoneNumberRegex], max_length = 13, unique = True)
    is_super         = models.PositiveIntegerField(default=0)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated          = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
