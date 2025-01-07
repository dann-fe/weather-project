from django.db import models

class County(models.Model):
    title = models.CharField(max_length=25, null=False)     
    latitude = models.CharField(max_length=8, null=False, default="0.0")     
    longitude = models.CharField(max_length=8, null=False, default="0.0")                

    def __str__(self):
        return self.title
class Weather(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=8, null=False, default="0.0")
    longitude = models.CharField(max_length=8, null=False, default="0.0")
    temperature = models.CharField(max_length=8, null=False, default="0.0")
