from app.model.seed import Seed
from app import db

def get_product(id):
    return Seed.get(id)

def get_product_quantity(id):
    return Seed.get_qty(id)

def minus_stock(id, quantity):
    anyvar = db.session.query(Seed).filter(Seed.id==id).first()
    anyvar.minus_qty(quantity) 