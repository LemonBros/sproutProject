from app import app 
from flask import render_template, request
from app.controller.product_controller import get_product
from app.model.seed_dict import seed_info

@app.route('/product')
def product():
    id = request.args.get('id')
    product = get_product(id)
    return render_template('seed/product.html', seed_type = "strawberry", seed_info = seed_info, product = product)