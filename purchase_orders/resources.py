from flask import Flask, jsonify
from flask_restful import Api, Resource


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


class PurchaseOrders(Resource):
  def get(self):
    return jsonify(purchase_orders)


