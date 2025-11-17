from flask import Flask, jsonify, request


app = Flask(__name__)

purchase_orders = [{
    'id': 1,
    'description': 'Pedido de Compra 1',
    'items': [
      {
        'id': 1,
        'description': 'Item do  pedido 1',
        'price': 20.99
      }
    ]
  }
]


# GET purchase_orders
# GET purchase_orders_by_id
# POST purchase_orders
# GET purchase_orders_items
# POST purchase_orders_items


@app.route('/')
def home():
  return "Olá mundo!"


@app.route('/purchase_orders', methods=['GET'])
def get_purchase_orders():
  return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>', methods=['GET'])
def get_purchase_orders_by_id(id):
  for po in purchase_orders:
    if po['id'] == id:
      return jsonify(po)
    
  return jsonify({'message': f'Pedido {id} não foi encontrado'})


@app.route('/purchase_orders', methods=['POST'])
def post_purchase_orders():
  request_data = request.get_json()

  purchase_order = {
    "id": request_data['id'],
    "description": request_data["description"],
    "items": []
  }

  purchase_orders.append(purchase_order)

  return jsonify(purchase_order)


@app.route('/purchase_orders/<int:id>/items', methods=['GET'])
def purchase_orders_items(id):
  for po in purchase_orders:
    if po['id'] == id:
      return jsonify(po['items'])
    
  return jsonify({'message': f'Itens do pedido {id} não foi encontrado'})


app.run(port=5000, debug=True)