from django.db import models

class TempHumi(models.Model):
    temp = models.FloatField(null=False, blank=False)
    humi = models.FloatField(null=False, blank=False)

class Gps(models.Model):
    lat  = models.FloatField(null=False, blank=False) #위
    lng  = models.FloatField(null=False, blank=False) #경도
    
  