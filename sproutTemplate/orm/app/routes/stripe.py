from app import app
import stripe
from flask import render_template, jsonify
import os


@app.route('/checkout')
def checkout():
    stripe.api_key = "sk_test_51IRpyvJPjBOs8E64GrvdG9FN5b34EBHhLRUTDvyebzfN9cir7V8t8SbVJ5Yj9g872boSnG1ErV0rWi5q6vKQwD5800elLLgsPd"

    intent = stripe.PaymentIntent.create(
    amount=1000,
    currency='usd',
    payment_method_types=['card'],
    receipt_email='jenny.rosen@example.com',
    )
    print(intent)
    return "it worked"

@app.route('/paypage')
def paypage():
    return render_template('/checkout/index.html')


@app.route('/success')
def success():
    return render_template('/checkout/success.html')


@app.route('/cancel')
def cancel():
    return render_template('/checkout/cancel.html')

stripe.api_key = 'sk_test_51IRpyvJPjBOs8E64GrvdG9FN5b34EBHhLRUTDvyebzfN9cir7V8t8SbVJ5Yj9g872boSnG1ErV0rWi5q6vKQwD5800elLLgsPd'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:5000/success',
    cancel_url='https://localhost:5000/cancel',
  )

  return jsonify(id=session.id)
