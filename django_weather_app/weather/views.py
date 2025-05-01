import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found!'}
    return render(request, 'weather.html', {'weather_data': weather_data})
