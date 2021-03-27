from app import app 

from app.controller.home_controller import home_controller
# home page route
@app.route('/')
@app.route('/home')
def home():
    return home_controller.index()

    