from app import db

class Seed(db.Model):

    #id is the primary key column for the Shoe model
    id = db.Column(db.Integer, primary_key=True)
    # #indexing the size column
    name = db.Column(db.String(50), index=True, unique=True)

    # #VARCHAR(80)
    # TODO:control type into Vegetable, Fruit, Flower 
    seed_type = db.Column(db.String(50), index=True)

    # #model must be unique for the Shoe
    price = db.Column(db.Integer, index=True)

    quantity = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Name {}, Type {}, Price {}, Quantity {}, Id {}>'.format(self.name, self.seed_type, self.price, self.quantity, self.id)
    
    #method to save the shoe
    def save(self):
    #     #saving the shoe, insert row into Shoe table
        db.session.add(self)
    #     #commit the transaction
        db.session.commit()

        return self.id

    def get_all():
    #     #get all the shoes from the database
        return Seed.query.all()

    @staticmethod
    def get_by_type(seed_type):
        data = db.session.query(Seed.id, Seed.name, Seed.price, Seed.quantity).filter(Seed.seed_type == seed_type).all()
        inventory = [{'id': item[0], 'name': item[1], 'price': item[2], 'qty': item[3]} for item in data]
        return inventory

    def delete(id):
        seed = Seed.get(id=id)
        db.session.delete(seed)
        db.session.commit()
    
    @staticmethod
    def get(id):
        seed = db.session.query(Seed).filter(Seed.id == id).first()
        return {'id': seed.id, 'name': seed.name, 'price': seed.price, 'qty': seed.quantity}
    
    def update(self):
        db.session.commit()

    def minus_quantaty(self, num):
        self.quantity -= num
        db.session.commit()
