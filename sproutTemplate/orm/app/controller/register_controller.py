from app import db
from app.model.register import RegistrationForm
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from app.model.login import User, LoginForm

# contfrolls the registration and adds new user to the database
class RegisterController():
    def register(self):
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        return render_template('registration/register.html', title='Register', form=form)

register_controller = RegisterController()