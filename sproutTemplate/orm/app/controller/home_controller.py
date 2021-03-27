#import flask dependancies
from flask import render_template, url_for


class HomeController(object):
    def index(self):
        #return the home page.
        return render_template("home/index.html", title='Home')
        
    

home_controller = HomeController()
