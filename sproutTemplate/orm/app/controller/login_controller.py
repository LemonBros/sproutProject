from flask_login import current_user, login_user, user_logged_out
from app.model.login import User, LoginForm
from flask import render_template, redirect, url_for, flash

class LoginController(object):
    def login(self):
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('home'))
        return render_template('login/login.html', title='Sign In', form=form)

login_controller = LoginController()
