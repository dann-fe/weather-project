from django.contrib import admin
from weather import models

admin.site.register(models.County)
admin.site.register(models.Weather)