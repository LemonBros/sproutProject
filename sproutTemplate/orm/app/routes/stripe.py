from app import app
import stripe
from flask import render_template, jsonify, redirect, url_for
import os
from app.model.cart_item import CartItem
from flask_login import current_user, login_required
from app.model.login import User
from app.controller.product_controller import ProductController
from app.controller.cart_controller import CartController


@app.route('/checkout')
@login_required
def checkout():
    stripe.api_key = "sk_test_51IRpyvJPjBOs8E64GrvdG9FN5b34EBHhLRUTDvyebzfN9cir7V8t8SbVJ5Yj9g872boSnG1ErV0rWi5q6vKQwD5800elLLgsPd"
    intent = stripe.PaymentIntent.create(
    amount=1000,
    currency='usd',
    payment_method_types=['card'],
    receipt_email=User.get_email(current_user.id),
    )

    return "it worked"

@app.route('/paypage')
@login_required
def paypage():
    return render_template('/checkout/index.html')


@app.route('/success')
@login_required
def success():
    whatever = CartItem.get_for_user(current_user.id)
    for i in range(0, len(whatever)):
        seed_id = whatever[i]['id']
        quantity = whatever[i]['qty']    
        ProductController.minus_stock(seed_id, quantity)
    CartItem.clear_on_logout(current_user.id)   
    return render_template('/checkout/success.html')


@app.route('/cancel')
@login_required
def cancel():
    return redirect(url_for('get_cart'))

stripe.api_key = 'sk_test_51IRpyvJPjBOs8E64GrvdG9FN5b34EBHhLRUTDvyebzfN9cir7V8t8SbVJ5Yj9g872boSnG1ErV0rWi5q6vKQwD5800elLLgsPd'

@app.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
  cart_items = CartItem.get_for_cart(current_user.id)
  empty_list = []
  for i in range(0,len(cart_items)):
        any_name = {
        'price_data': {
          'currency': 'usd',
          'product_data': {
            # replace with item 0
            'name': cart_items[i]['name'],
          },
          # replace with item 1
          'unit_amount': (cart_items[i]['price']*100),
        },
        # replace with item 2
        'quantity': cart_items[i]['quantity'],
      }
        empty_list.append(any_name) 
  session = stripe.checkout.Session.create(
    billing_address_collection='auto',
    shipping_address_collection={
    'allowed_countries': ['US', 'CA'],
  },
    payment_method_types=['card'],
    line_items=empty_list,
    mode='payment',
    success_url='https://sprout-seed.me/success',
    cancel_url='https://sprout-seed.me/cancel',
  )

  return jsonify(id=session.id)
