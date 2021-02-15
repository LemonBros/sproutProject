from app import app
from app.controller.shoe_controller import shoe_controller
@app.route('/shoe')
def shoe():
    return shoe_controller.index()