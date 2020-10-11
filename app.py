from flask import Flask, jsonify, request
from products import products
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

# Obtencion del objeto products


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"message": "Product's list", "products": products})


# obtencion del objeto por parametro
@app.route('/products/<product_name>')
def search_product(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name
    ]
    if len(productsFound) > 0:
        return jsonify({"product": productsFound[0]})
    return jsonify({'message': 'product not found'})


# Creacion de objeto
@app.route('/products/create', methods=['POST'])
def create_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'message': 'Product added successfully', 'products': products})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
