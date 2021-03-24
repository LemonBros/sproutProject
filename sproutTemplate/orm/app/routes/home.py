from app import app 

from app.controller.home_controller import home_controller

@app.route('/')
@app.route('/home')
def home():
    return home_controller.index()

    