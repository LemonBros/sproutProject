from app import app
import stripe
from flask import render_template, jsonify
import os
from app.model.cart_item import CartItem
from flask_login import current_user
from app.model.login import User
from app.controller.product_controller import *


@app.route('/checkout')
def checkout():
    stripe.api_key = "sk_test_51IRpyvJPjBOs8E64GrvdG9FN5b34EBHhLRUTDvyebzfN9cir7V8t8SbVJ5Yj9g872boSnG1ErV0rWi5q6vKQwD5800elLLgsPd"
    intent = stripe.PaymentIntent.create(
    amount=1000,
    currency='usd',
    payment_method_types=['card'],
    receipt_email=User.get_email(current_user.id),
    )
    print(intent)
    return "it worked"

@app.route('/paypage')
def paypage():
    return render_template('/checkout/index.html')


@app.route('/success')
def success():
    whatever = CartItem.get_for_user(current_user.id)
    for i in range(0, len(whatever)):
        seed_id = whatever[i]['id']
        quantity = whatever[i]['qty']    
        minus_stock(seed_id, quantity)
    CartItem.clear_on_logout(current_user.id)   
    return render_template('/home/index.html')


@app.route('/cancel')
def cancel():
    return render_template('/checkout/cancel.html')

stripe.api_key = 'sk_test_51IRpyvJPjBOs8E64GrvdG9FN5b34EBHhLRUTDvyebzfN9cir7V8t8SbVJ5Yj9g872boSnG1ErV0rWi5q6vKQwD5800elLLgsPd'

@app.route('/create-checkout-session', methods=['POST'])
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
  print("cart_items is ", cart_items) 
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=empty_list,
    mode='payment',
    success_url='http://localhost:5000/success',
    cancel_url='https://localhost:5000/cancel',
  )

  return jsonify(id=session.id)
