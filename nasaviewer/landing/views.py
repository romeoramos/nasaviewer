from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import date, timedelta

# Create your views here.

def index(request):
    yesterday = str(date.today() - timedelta(days=1))
    values = {'start_date':yesterday,'end_date':yesterday,'api_key':'hTcesBBBIuHHXsLgRxN4T29W2q4Db5DBE9jwr3bQ'}
    nasa_api = requests.get('https://api.nasa.gov/neo/rest/v1/feed',params=values)
    nasa_json = nasa_api.json()
    asteroids = nasa_json['near_earth_objects'][yesterday]
    return render(request, 'landing/index.html',{'asteroids':asteroids,'yesterday':yesterday})
