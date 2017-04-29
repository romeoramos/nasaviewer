from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):

    values = {'start_date':'2017-04-27','end_date':'2017-04-27','api_key':'hTcesBBBIuHHXsLgRxN4T29W2q4Db5DBE9jwr3bQ'}
    nasa_api = requests.get('http://api.nasa.gov/neo/rest/v1/feed',params=values)
    asteroids = nasa_api.json()
    print(asteroids['near_earth_objects']['2017-04-26']['links'])
    return render(request, 'landing/index.html',{'asteroids':asteroids})
