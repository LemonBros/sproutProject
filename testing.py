from flask import Flask, render_template
from livereload import Server

cart = Flask(__name__)

@cart.route("/")
def index():
    data = [
        {
            'n':1,
            'name':'Rose seeds',
            'price':13.5,
            'qty':2,
            'cost':27
        },
        {
            'n':2,
            'name':'Orange seeds',
            'price':24,
            'qty':3,
            'cost':72
        }

    ]

    return render_template("cart.html", members=data)

if __name__ == "__main__":
    server = Server(cart.wsgi_app)
    server.watch('templates/*.html')
    server.watch('static/styles/*.css')
    server.serve(port=5555)

