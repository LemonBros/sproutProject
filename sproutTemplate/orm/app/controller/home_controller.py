#import flask dependancies
from flask import render_template, url_for


# from random import randint

#import what you need from the model package
# from app.model import Home

#controls the shoe logic
class HomeController(object):
    def index(self):
        #return a view passed with the data of shoes.
        return render_template("home/index.html")
        
    

home_controller = HomeController()
