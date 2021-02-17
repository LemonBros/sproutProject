from app import db

class Shoe(db.Model):

    #id is the primary key column for the Shoe model
    id = db.Column(db.Integer, primary_key=True)
    #indexing the size column
    size = db.Column(db.Float, index=True)

    #VARCHAR(80)
    brand = db.Column(db.String(80), index=True)

    #model must be unique for the Shoe
    model = db.Column(db.String(89), index=True, unique=True)

    #method to save the shoe
    def save(self):
        #saving the shoe, insert row into Shoe table
        db.session.add(self)
        #commit the transaction
        db.session.commit()

        return self.id

    def get_all():
        #get all the shoes from the database
        return Shoe.query.all()
