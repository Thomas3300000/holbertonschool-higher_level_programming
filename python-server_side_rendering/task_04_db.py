from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open ('items.json') as file:
        data = json.load(file)
        items_list = data.get('items', [])
        return render_template('items.html', items=items_list)
    
def read_json():
    with open ('products.json') as f:
        products = json.load(f)
    return products

def read_csv():
    products = []
    with open ('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row['id']),
                "name": row['name'],
                "category": row['category'],
                "price": float(row['price'])
            })
    return products

def read_sql():
    products = []
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    conn.close()
    for row in prod:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })
    return products

@app.route('/products')
def products_display():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error='Wrong source')
        
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)
