from django.db import models

class County(models.Model):
    title = models.CharField(max_length=25)     
    latitude = models.CharField(max_length=15)                  # poloha okresu vzdy bude na okresnim meste
    longitude = models.CharField(max_length=15)                 # poloha okresu vzdy bude na okresnim meste
    
class Weather(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=8)
