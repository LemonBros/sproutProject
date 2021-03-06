from app import db
from app.model.login import User
from app.model.seed import Seed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class CartItem(db.Model):
    seed_id = db.Column(db.Integer, db.ForeignKey('seed.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    quantity = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Number{}, Name {}, Type {}, Price {}, Quantity {}>'.format(self.id, self.name, self.seed_type, self.price, self.quantity)
    
    def save(self):
    #     #saving the shoe, insert row into Shoe table
        db.session.add(self)
    #     #commit the transaction
        db.session.commit()

    @staticmethod
    def get_for_user(user_id):
        return CartItem.query.filter_by(user_id = user_id).all()

    @staticmethod
    def delete(id):
        seed = Seed.get(id=id)
        db.session.delete(seed)
        db.session.commit()
    
    def update(self):
        db.session.commit()

class CartForm(FlaskForm):
    pass
