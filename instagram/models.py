from distutils.command.upload import upload
from email import message
from tokenize import blank_re
from django.db import models

class Post(models.Model):
    message    = models.TextField()
    photo      = models.ImageField(blank=True, upload_to='instagram/post/%y년/%m월/%d일') # 파일 경로를 저장하는거임!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self): #str 메소드 오버라이딩
        return f"내용:{self.message}"