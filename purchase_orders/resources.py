from flask import jsonify
from flask_restful import Resource

purchase_orders = [
  {
    'id': 1,
    'description': 'Pedido nro 1',
    'items': [
      {
        'id': 1,
        'description': 'Items nro 1',
        'price': 19.99
      }
    ]
  }
]


class PurchaseOrders(Resource):

  def get(self):
    return jsonify(purchase_orders)