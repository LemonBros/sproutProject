from flask import render_template, redirect
from app.model.cart_item import CartItem
from flask_login import current_user
from app.controller.product_controller import get_product_quantity
from app import db

class CartController:

    @staticmethod
    def get_all():
        if current_user.is_authenticated:
            return render_template('cart/cart.html', title='Cart', members=CartItem.get_for_user(current_user.id))
        else:
            return redirect(url_for('login'))

    @staticmethod
    def add(seed_id, quantity):
        seed_stock = get_product_quantity(seed_id)
        if current_user.is_authenticated:
            if quantity > seed_stock:
                return {"reply": "Quantity Error Stock Too Low"}
            else:
                item = CartItem()
                item.seed_id = seed_id
                item.user_id = current_user.id
                item.quantity = quantity
                item.save()
            return {"reply": "Successfully Added To Cart"}
        return {"reply": ""}

    @staticmethod
    def delete(user_n, item_removed):
        CartItem.delete_row(user_n, item_removed)

    @staticmethod
    def update(user_n, item_removed, qty):
        CartItem.update_row(user_n, item_removed, qty)
    
    @staticmethod
    def clear_cart(userid):
        CartItem.clear_on_logout(userid)
        

