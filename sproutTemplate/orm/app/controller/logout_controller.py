from flask_login import logout_user, login_required, current_user
from flask import url_for, redirect, session
from app import app, login, db
from app.controller.cart_controller import CartController

@app.route('/logout')
@login_required
def logout():
    userid = current_user.id
    CartController.clear_cart(userid)
    logout_user()
    return redirect(url_for('home'))