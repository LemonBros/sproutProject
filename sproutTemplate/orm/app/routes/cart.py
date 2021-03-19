from app import app
from app.model.cart_item import CartItem
from app.controller.product_controller import ProductController
from app.controller.cart_controller import CartController
from flask import request, redirect, url_for, request, flash
from flask_login import current_user, login_required

@app.route("/get_cart", methods=['GET'])
@login_required
def get_cart():
    return CartController.get_all()

@app.route("/add_to_cart", methods=['POST'])
@login_required
def add_to_cart():
    seed = request.args.get('seed_id')
    quantity = request.args.get('quantity', type=int)
    return CartController.add(seed, quantity)

@app.route("/removed/<int:item_removed>", methods=['POST'])
@login_required
def removed(item_removed):
    user_n = current_user.id
    qty = request.form.get('qty', type=int)
    seed_stock = ProductController.get_product_quantity(item_removed)
    if qty > seed_stock:
        flash('QTY error')
        return redirect(url_for('get_cart'))
    else:
        if qty > 0:
            CartController.update(user_n, item_removed, qty)
        else:
            CartController.delete(user_n, item_removed)
        return redirect(url_for('get_cart'))

    
