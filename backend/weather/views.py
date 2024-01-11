from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class WeatherAPIView(APIView):
    @cache_page(1800)
    def get(self, request):
        city_name = request.GET.get('city', '')
        if not city_name:
            return JsonResponse({'error': 'Необходимо написать город'}, status=400)

        api_key = '931b9e6d54f671287353d688f0893785'
        base_url = 'http://api.openweathermap.org/data/2.5/weather'

        response = requests.get(f'{base_url}?q={city_name}&appid={api_key}&units=metric')
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'температура': data['main']['temp'],
                'давление': data['main']['pressure'],
                'скорость_ветра': data['wind']['speed'],
            }
            return JsonResponse(weather_data)
        else:
            return JsonResponse({'error': 'Не удалось получить данные(( '}, status=response.status_code)
