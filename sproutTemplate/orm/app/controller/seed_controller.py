# TODO : do this, do that, im reza
from flask import render_template, url_for

class SeedController(object):
    def index(self):
        #return a view passed with the data of shoes.
        return render_template("seed/index.html")