from flask import Flask, jsonify
from products import products
app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
