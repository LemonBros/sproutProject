from flask import render_template
from app.model.seed import Seed

class ProductController():
    def get_product(id):
        return Seed.get(id)

    def get_product_quantity(id):
        return Seed.get_qty(id)

    def get(id):
        seeds = Seed.get(id)
        seeds['imagePath'] = "images/%s.png" % (seeds['name'])
        return seeds

    