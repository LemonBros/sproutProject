from app import db, app
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
        return '<User id {}, seed id {}, quantity {}>'.format(self.user_id, self.seed_id, self.quantity)
    
    def save(self):
    #     #saving the shoe, insert row into Shoe table
        db.session.add(self)
    #     #commit the transaction
        db.session.commit()

    @staticmethod
    def get_for_user(user_id):
        items = CartItem.query.filter_by(user_id = user_id).all()
        result = [{'user_id': item.user_id, 'seed_id': item.seed_id, 'quantity': item.quantity} for item in items]
        app.logger.error("items: {}".format(result))
        return result

    @staticmethod
    def delete(id):
        seed = Seed.get(id=id)
        db.session.delete(seed)
        db.session.commit()
    
    def update(self):
        db.session.commit()

class CartForm(FlaskForm):
    pass
