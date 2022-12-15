from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Weather App Comming soon"

if __name__=="__main__":
    app.run(debug=True)