from app import app 
from flask import render_template
from app.model.seed_dict import seed_info

@app.route('/product2')
def product2():
    seed_info_display = seed_info
    return render_template('seed/product.html', seed_type = "berry", seed_info = seed_info_display)