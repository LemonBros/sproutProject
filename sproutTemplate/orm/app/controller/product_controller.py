from app.model.seed import Seed


def get_product(id):
    return Seed.get(id)

def get_product_quantity(id):
    return Seed.get_qty(id)