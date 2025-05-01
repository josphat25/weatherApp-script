# weatherApp-script
## Django Project
django-admin startproject weather_project
cd weather_project
python manage.py startapp weather
## Structure
weather_project/

├── weather_project/

│   ├── settings.py

│   └── urls.py

├── weather/

│   ├── views.py

│   ├── urls.py

│   └── templates/

│       └── weather.html
└── manage.py

## settings.py
Add 'weather', to INSTALLED_APPS.

## URLs

from django.contrib import admin

from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('', include('weather.urls')),  # include app urls
    
]

## weather/urls.py

from django.urls import path

from . import views

urlpatterns = [

    path('', views.weather_view, name='weather'),
    
]

## weather/views.py

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

  ## weather/templates/weather.html

  <!DOCTYPE html>
  
<html>
  
<head>
  
    <title>Weather App</title>
    
</head>

<body>
  
    <h1>Check Weather</h1>
    
    <form method="POST">
    
        {% csrf_token %}
        
        <input type="text" name="city" placeholder="Enter city name">
        
        <button type="submit">Get Weather</button>
        
    </form>

    {% if weather_data.city %}
    
        <h2>Weather in {{ weather_data.city }}</h2>
        
        <p>Temperature: {{ weather_data.temperature }}°C</p>
        
        <p>Description: {{ weather_data.description }}</p>
        
        <img src="http://openweathermap.org/img/wn/{{ weather_data.icon }}@2x.png" alt="Icon">
        
    {% elif weather_data.error %}
    
        <p>{{ weather_data.error }}</p>
        
    {% endif %}
    
</body>

</html>
##  



