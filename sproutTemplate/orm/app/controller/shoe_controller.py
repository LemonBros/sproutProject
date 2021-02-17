#import flask dependancies
from flask import render_template

from random import randint

#import what you need from the model package
from app.model import Shoe

#controls the shoe logic
class ShoeController(object):
    def index(self):
        shoes = Shoe.get_all()
        for shoe in shoes:
            print(shoe.id, shoe.size, shoe.brand, shoe.model)
        
        #return a view passed with the data of shoes.
        return render_template("shoe/index.html", shoes=shoes)

    def save(self):
        #create a show
        shoe = Shoe(size=12, brand="addidas", model='yeezy%d' % (randint(0,1000)))

        #save the show
        shoe_id = shoe.save()

        print("SHOE ID", shoe_id)

        #display save page
        return render_template("shoe/save.html")


shoe_controller = ShoeController()
