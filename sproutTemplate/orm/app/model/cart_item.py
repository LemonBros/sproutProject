from app import db, app
from app.model.login import User
from app.model.seed import Seed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from sqlalchemy import select

class CartItem(db.Model):
    seed_id = db.Column(db.Integer, db.ForeignKey('seed.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    quantity = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User id {}, seed id {}, quantity {}>'.format(self.user_id, self.seed_id, self.quantity)
    
    def save(self):
    #     #saving the shoe, insert row into Shoe table
        db.session.add(self)
    #     #commit the transaction
        db.session.commit()

    @staticmethod
    def get_for_user(user_id):
        items = db.session.query(CartItem.quantity, Seed.name, Seed.price).filter(CartItem.user_id == user_id).filter(CartItem.seed_id == Seed.id).all()
        
        '''
        result0 = []
        for i in range(len(items)):
            item = items[i]
            result0.append({'quantity': item[0], 'name': item[1], 'price': item[2], 'cost': item[0]*item[2], 'n': i+1})
        app.logger.error("result0: {}".format(result0))
        '''

        # list comprehension.
        # enumerate() is a function used to add indices to list elements
        result = [{'qty': item[0], 'name': item[1], 'price': item[2], 'cost': item[0]*item[2], 'n': i+1} for i, item in enumerate(items)]
        app.logger.error("result: {}".format(result))
        return result

    @staticmethod
    def delete(id):
        cart = CartiItem.get(seed_id=id)
        db.session.delete(cart)
        db.session.commit()
    
    def update(self):
        db.session.commit()

class CartForm(FlaskForm):
    pass
