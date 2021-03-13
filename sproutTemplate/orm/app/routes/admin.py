from app import app, login
from app.controller.admin_controller import admin_controller
from flask_login import login_required


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return admin_controller.seedregister()

@app.route('/adminupdate', methods=['GET', 'POST'])
@login_required
def adminupdate():
    return admin_controller.seedupdate()