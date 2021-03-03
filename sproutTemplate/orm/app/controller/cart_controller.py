from flask import render_template
from cart_item import CartItem
from flask_login import current_user

class CartController:

    @staticmethod
    def get_all():
        return render_template('cart/cart.html', title='Cart', members=[])

    @staticmethod
    def add(seed_id):
        if current_user.is_authenticated:
            item = CartItem()
            item.seed_id = seed_id
            item.user_id = current_user.id
            item.save()