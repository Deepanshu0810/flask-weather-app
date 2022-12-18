import requests
from flask import Flask,render_template,url_for
import creds
app=Flask(__name__)

@app.route('/')
def welcome():
    city='London'
    api = f'http://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={creds.api_key}'
    r=requests.get(api).json()
    print(r)
    return render_template("weather.html")


if __name__=="__main__":
    app.run(debug=True)