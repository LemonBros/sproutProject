from app import app
from app.model.cart_item import CartItem
from app.controller.cart_controller import CartController
from flask import request

@app.route("/get_cart", methods=['GET'])
def get_cart():
    return CartController.get_all()

@app.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    seed = request.args.get('seed_id')
    quantity = request.args.get('quantity', 1)
    return CartController.add(seed, quantity)

@app.route("/get_cart/<user_n>/<item_removed>", methods=['DELETE', 'POST', 'GET'])
def delete(user_n, item_removed):
    CartController.delete(user_n, item_removed)
    return CartController.get_all()
