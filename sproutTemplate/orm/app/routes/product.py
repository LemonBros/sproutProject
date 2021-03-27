from app import app 
from flask import render_template, request
from app.controller.product_controller import ProductController
from app.model.seed_dict import seed_info
# shows the product page which returns items for the html page to show
@app.route('/product')
def product():
    seed_type = request.args.get('seed_type')
    id = request.args.get('id')
    product = ProductController.get(id)
    name = product['name']
    return render_template('seed/product.html', seed_type = seed_type, seed_info = seed_info, product = product, title= name)