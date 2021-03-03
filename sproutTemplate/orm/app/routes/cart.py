from app import app
from app.model.cart_item import CartItem
from app.controller.cart_controller import CartController

@app.route("/cart")
def cart():
    return CartController.get_all()