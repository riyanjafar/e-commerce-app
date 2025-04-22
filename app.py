from flask import Flask, render_template

app = Flask(__name__)

urunler = [
    {'id': 1, 'name': 'Akıllı Telefon', 'price': 1000},
    {'id': 2, 'name': 'Dizüstü Bilgisayar', 'price': 5000}
]
@app.route('/')
def ana_sayfa():
    return render_template('index.html', urunler=urunler)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
