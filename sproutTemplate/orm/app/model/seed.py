from app import db
from app.model.cart_item import cart_item

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
        return '<Name {}, Type {}, Price {}, Quantity {}>'.format(self.name, self.seed_type, self.price, self.quantity)
    
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

    def delete(id):
        seed = Seed.get(id=id)
        db.session.delete(seed)
        db.session.commit()
    
    def get(id):
        return db.session.query(Seed).filter(Seed.id == id).first()
    
    def update(self):
        db.session.commit()

    def minus_quantaty(self, num):
        self.quantity -= num
        db.session.commit()
