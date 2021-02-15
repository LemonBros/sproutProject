from flask import render_template

from app.model import Shoe

class ShoeController(object):
    def index(self):
        shoes = Shoe.get_all()

        return render_template("shoe/index.html", shoes=shoes)

shoe_controller = ShoeController()