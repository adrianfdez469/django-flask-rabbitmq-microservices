from producer import publish
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)
 
@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    products = Product.query.all()
    print(products)
    return jsonify(products)

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://host.docker.internal:8000/api/user')
    json = req.json()

    try:
      product_user = ProductUser(user_id=json['id'], product_id=id)
      db.session.add(product_user)
      db.session.commit()

      # event
      publish('product_like', id)

    except:
      abort('400', 'You already like this product')


    return jsonify({
      "message": "success"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
