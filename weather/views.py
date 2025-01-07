from django.shortcuts import render, get_object_or_404
from weather.models import County, Weather
from decouple import config
import requests
from django.views.decorators.cache import cache_page

def county_list(request):
    counties = County.objects.all()
    context = {"counties": counties}
    return render(request, 'index.html', context)


OWM_API_KEY = config('OWM_API_KEY')

@cache_page(60 * 300)
def get_weather_data(request, pk):
    county = get_object_or_404(County, pk=pk)

    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={county.latitude}&lon={county.longitude}&units=metric&appid={OWM_API_KEY}"
    response = requests.get(weather_url)
    data = response.json()
    temperature = round(data["current"]["temp"])

    weather_data = Weather.objects.update_or_create(
        county=county,
        latitude=county.latitude, 
        longitude=county.longitude,
        defaults={
            "temperature": temperature
        }
        )
    context = {
        "temperature": temperature,
        "county": county,
    }
    return render(request, 'county_weather.html', context)