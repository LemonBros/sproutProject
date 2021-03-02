from app import app 
from flask import render_template

@app.route('/vegetable')
def vegetable():
    seed_type = "vegetable"
    return render_template('gallery-tab/gallery.html', seed_type = seed_type)

