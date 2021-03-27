from app import app
from app.controller.product_controller import ProductController
from app.controller.cart_controller import CartController
from flask import request, redirect, url_for, request, flash
from flask_login import current_user, login_required
# this is the routes for the cart. for each function you need to be logged in to use
# this will get the cart controller
@app.route("/get_cart", methods=['GET'])
@login_required
def get_cart():
    return CartController.get_all()
# this will add to the cart
@app.route("/add_to_cart", methods=['POST'])
@login_required
def add_to_cart():
    seed = request.args.get('seed_id')
    quantity = request.args.get('quantity', type=int)
    return CartController.add(seed, quantity)
# removes the item from the cart
@app.route("/removed/<int:item_removed>", methods=['POST'])
@login_required
def removed(item_removed):
    user_n = current_user.id
    qty = request.form.get('qty', type=int)
    seed_stock = ProductController.get_product_quantity(item_removed)
    # checks the stock when removed
    if qty > seed_stock:
        flash('QTY error')
        return redirect(url_for('get_cart'))
    else:
        if qty > 0:
            CartController.update(user_n, item_removed, qty)
        else:
            CartController.delete(user_n, item_removed)
        return redirect(url_for('get_cart'))

    
