from flask import Flask, render_template, redirect, url_for
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Akıllı Telefon', 'price': 1000},
    {'id': 2, 'name': 'Dizüstü Bilgisayar', 'price': 5000}
]

cart = []

page_views = Counter('page_views', 'Sayfa görüntüleme sayısı', ['page'])
add_to_cart_counter = Counter('add_to_cart_total', 'Sepete ekleme sayısı')

@app.route('/')
def home():
    page_views.labels(page='home').inc()
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        add_to_cart_counter.inc()
        return redirect(url_for('view_cart'))
    return "Ürün bulunamadı"

@app.route('/cart')
def view_cart():
    page_views.labels(page='cart').inc()
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
