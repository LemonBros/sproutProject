from flask_login import logout_user, login_required
from flask import url_for, redirect, session
from app import app, login

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))