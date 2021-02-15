class Shoe(object):
    shoes = []

    def __init__(self, size, brand):
        self.size = size
        self.brand = brand

        Shoe.shoes.append(self)

    def get_all():
        return Shoe.shoes