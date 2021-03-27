from app import app 
from flask import render_template
# to view the flower page
@app.route('/flower')
def flower():
    seed_type = "flower"
    return render_template('gallery-tab/gallery.html', seed_type = seed_type)

