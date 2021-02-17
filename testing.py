from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sproutHomepage/home.html")


@app.route("/cart")
def cart():
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

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('templates/*.html')
    server.watch('static/styles/*.css')
    server.serve(port=5555)

