from app import app, login
from flask_login import current_user, login_user
from app.controller.login_controller import login_controller

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_controller.login()