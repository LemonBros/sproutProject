from app import db

class User(db.Model):

    #id is the primary key column for the Shoe model
    id = db.Column(db.Integer, primary_key=True)
    # #indexing the size column
    username = db.Column(db.String(50), index=True, unique=True)

    # #VARCHAR(80)
    email = db.Column(db.String(50), index=True, unique=True)

    # #model must be unique for the Shoe
    password_hash = db.Column(db.String(90))

    def __repr__(self):
        return '<User {}><Email and ID {} {}>'.format(self.username, self.email, self.id)
    
    #method to save the shoe
    def save(self):
    #     #saving the shoe, insert row into Shoe table
        db.session.add(self)
    #     #commit the transaction
        db.session.commit()

        return self.id

    def get_all():
    #     #get all the shoes from the database
        return User.query.all()

    def delete(id):
        user = User.get(id=id)
        db.session.delete(user)
        db.session.commit()
    
    def get(id):
        return db.session.query(User).filter(User.id == id).first()
    
    def update(self):
        db.session.commit()