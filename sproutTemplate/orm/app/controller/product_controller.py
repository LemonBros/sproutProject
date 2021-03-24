from flask import render_template
from app.model.seed import Seed
from app import db

class ProductController():
    def get_product(id):
        return Seed.get(id)

    def get_product_quantity(id):
        return Seed.get_qty(id)

    def get(id):
        seeds = Seed.get(id)
        seeds['imagePath'] = "images/%s.png" % (seeds['name'])
        return seeds

    def minus_stock(id, quantity):
        anyvar = db.session.query(Seed).filter(Seed.id==id).first()
        anyvar.minus_qty(quantity) 
