from app import db, app
from app.model.login import User
from app.model.seed import Seed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from sqlalchemy import select
# the functios names discribes what they do.
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
        items = db.session.query(CartItem.quantity, CartItem.seed_id, Seed.name, Seed.price).filter(CartItem.user_id == user_id).filter(CartItem.seed_id == Seed.id).all()
        
        '''
        result0 = []
        for i in range(len(items)):
            item = items[i]
            result.append({'quantity': item[0], 'name': item[1], 'price': item[2], 'cost': item[0]*item[2], 'n': i+1})
        app.logger.error("result0: {}".format(result0))
        '''

        # list comprehension.
        # enumerate() is a function used to add indices to list elements
        result = [{'qty': item[0],'id':item[1], 'name': item[2], 'price': item[3], 'cost': item[0]*item[3], 'n': i+1} for i, item in enumerate(items)]
        return result

    @staticmethod
    def delete_row(user_n, item_removed):
        cart = db.session.query(CartItem).filter(CartItem.user_id == user_n).filter(CartItem.seed_id==item_removed).first()
        db.session.delete(cart)
        db.session.commit()
    
    @staticmethod
    def update_row(user_n, item_removed, qty):
        cart = db.session.query(CartItem).filter(CartItem.user_id == user_n).filter(CartItem.seed_id==item_removed).first()
        cart.update_quantity(qty)
        db.session.commit()

    def update_quantity(self, qty):
        self.quantity = qty

    def clear_on_logout(userid):
        db.session.query(CartItem).filter(CartItem.user_id == userid).\
        delete(synchronize_session=False)
        db.session.commit()

    def get_for_cart(user_id):
        items = db.session.query(Seed.name, Seed.price, CartItem.quantity).filter(CartItem.user_id == user_id).filter(CartItem.seed_id == Seed.id).all()
        result = [{'name': item[0],'price':item[1], 'quantity': item[2],'n': i+1} for i, item in enumerate(items)]
        return result