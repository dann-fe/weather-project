from django.urls import path
from weather import views

urlpatterns = [
    path('', views.county_list, name='county_list'),
    path('weather/<int:pk>', views.get_weather_data, name='county_weather')
]
