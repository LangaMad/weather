from django.shortcuts import render
import requests, json
from .models import City
from .forms import CityForm
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(1800)
def index(request):
    cities = City.objects.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=931b9e6d54f671287353d688f0893785'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        temperature = city_weather.get('main', {}).get('temp')
        wind_speed = city_weather.get('wind', {}).get('speed')
        pressure = city_weather.get('main', {}).get('pressure')

        if temperature is not None and wind_speed is not None and pressure is not None:
            weather = {
                'city': city,
                'temperature': temperature,
                'wind_speed': wind_speed,
                'pressure': pressure,
            }
            weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)  # returns index.html template