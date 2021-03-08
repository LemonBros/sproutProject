from app.model.seed import Seed

def get_product(id):
    return Seed.get(id)
