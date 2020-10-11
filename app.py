from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run(debug=True, port=4000)
