from flask import Flask
import os

api_key = os.environ.get('API_KEY')

def create_app():
    app=Flask(__name__)
    
    from .views import views
    app.register_blueprint(views,url_prefix="/")

    return app