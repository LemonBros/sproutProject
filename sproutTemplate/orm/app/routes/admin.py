from app import app, login
from app.controller.admin_controller import admin_controller
from flask_login import login_required
# view the admin page

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return admin_controller.seedregister()

@app.route('/adminupdate', methods=['GET', 'POST'])
@login_required
def adminupdate():
    return admin_controller.seedupdate()

@app.route('/admindelete', methods=['GET', 'POST'])
@login_required
def admindelete():
    return admin_controller.seeddelete()