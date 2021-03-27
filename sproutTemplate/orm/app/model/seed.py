from app import db
# the seed database
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
    
    #method to save the seed
    def save(self):
    #     #saving the seed, insert row into Shoe table
        db.session.add(self)
    #     #commit the transaction
        db.session.commit()

        return self.id

    def get_all():
    #     #get all the seeds from the database
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
    
    def get_qty(id):
        seed = db.session.query(Seed).filter(Seed.id == id).first()
        return seed.quantity


    def minus_qty(self, quantity):
        self.quantity -= quantity

    # the methods beyond this are for the admin to use
    @staticmethod
    def adminupdate(seedname, quantity):
        adminseed = db.session.query(Seed).filter(Seed.id == seedname).first()
        adminseed.update_quantity(quantity)
    
    def update_quantity(self, quantity):
        self.quantity += quantity
        db.session.commit()
    
    @staticmethod
    def admindelete(seedname):
        admindeleteseed = db.session.query(Seed).filter(Seed.id==seedname).first()
        db.session.delete(admindeleteseed)
        db.session.commit()
    
