from app import app 
from flask import render_template
# shows the vegetable page
@app.route('/vegetable')
def vegetable():
    seed_type = "vegetable"
    return render_template('gallery-tab/gallery.html', seed_type = seed_type)

