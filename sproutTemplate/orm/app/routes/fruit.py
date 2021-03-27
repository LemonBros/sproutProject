from app import app 
from flask import render_template
# to view the fruit page
@app.route('/fruit')
def fruit():
    seed_type = "fruit"
    return render_template('gallery-tab/gallery.html', seed_type = seed_type)

