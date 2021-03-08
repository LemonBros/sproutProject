from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.model.seed import Seed

class CartForm(FlaskForm):
    seedname = StringField('Seed Name', validators=[DataRequired()])
    seed_type = StringField('Seed Type', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    quantity = SelectField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_seedname(self, seedname):
        seed = Seed.query.filter_by(name=seedname.data).first()
        if seed is not None:
            raise ValidationError('Please use a different seed name.')