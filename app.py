import requests
from flask import Flask,render_template,url_for
import os

api_key = os.environ.get('API_KEY')
app=Flask(__name__)

@app.route('/')
def welcome():
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
    return render_template("weather.html")


if __name__=="__main__":
    app.run(debug=True)