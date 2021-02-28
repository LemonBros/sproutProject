from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app import login


@login.user_loader
def user_loader(id):
    user = User.get(id)
    if user is None:
        flash('You have been automatically logged out')
        User.update()
    return User.query.get(int(id))

class User(UserMixin, db.Model):

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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')