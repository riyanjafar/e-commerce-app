from flask import Flask

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Telefon'},
    {'id': 2, 'name': 'Bilgisayar'},
    {'id': 3, 'name': 'Tablet'},
]

cart = []

@app.route('/')
def home():
   
    product_list = ', '.join([p['name'] for p in products])
    return f"Ürünler: {product_list}"

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
   
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        return f"{product['name']} sepete eklendi!"
    return "Ürün bulunamadı."

if __name__ == '__main__':
    app.run(debug=True)
