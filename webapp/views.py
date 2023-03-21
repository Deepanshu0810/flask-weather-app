from flask import Blueprint, render_template,request
import requests
from . import api_key

views = Blueprint('views',__name__)

@views.route("/",methods=['POST','GET'])
def home():
    city='London'
    api = f'http://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={api_key}'
    r=requests.get(api).json()

    if(r['cod']=='404'):
        weather = {'city' : 'City Not Found'}
    else:
        weather ={
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }

    print(weather)
    return render_template('weather.html')