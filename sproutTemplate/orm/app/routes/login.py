from app import app
from flask_login import current_user, login_user
from app.controller.login_controller import login_controller

@app.route('/login')
def login():
    return login_controller.login()