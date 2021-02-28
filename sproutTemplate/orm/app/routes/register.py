from app import app
from app.controller.register_controller import register_controller

@app.route('/register', methods=['GET', 'POST'])
def registration():
    return register_controller.register()