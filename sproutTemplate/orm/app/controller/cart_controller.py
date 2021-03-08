from flask import render_template, redirect
from app.model.cart_item import CartItem
from flask_login import current_user
from app.model.cart_item import CartItem

class CartController:

    @staticmethod
    def get_all():
        if current_user.is_authenticated:
            return render_template('cart/cart.html', title='Cart', members=CartItem.get_for_user(current_user.id))
        else:
            return redirect(url_for('login'))

    @staticmethod
    def add(seed_id, quantity):
        if current_user.is_authenticated:
            item = CartItem()
            item.seed_id = seed_id
            item.user_id = current_user.id
            item.quantity = quantity
            item.save()
            return {"reply": "oh yis"}
        return {"reply": "ololoshenki!"}

    def delete(seed_id):
        CartItem.delete(seed_id)
        return redirect(url_for("get_cart"))