from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Ürün listesi
urunler = [
    {'id': 1, 'name': 'Akıllı Telefon', 'price': 1000},
    {'id': 2, 'name': 'Dizüstü Bilgisayar', 'price': 5000}
]

# Alışveriş sepeti
sepet = []

@app.route('/')
def ana_sayfa():
    return render_template('index.html', urunler=urunler)

@app.route('/ekle/<int:urun_id>')
def sepete_ekle(urun_id):
    urun = next((u for u in urunler if u['id'] == urun_id), None)
    if urun:
        sepet.append(urun)
        return redirect(url_for('sepeti_goster'))
    return "Ürün bulunamadı"

@app.route('/sepet')
def sepeti_goster():
    toplam = sum(item['price'] for item in sepet)
    return render_template('cart.html', sepet=sepet, toplam=toplam)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
