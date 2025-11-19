from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from purchase_orders.resources import purchase_orders


class PurchaseOrdersItems(Resource):
  parser = reqparse.RequestParser()

  parser.add_argument('id', type=int, required=True, help='Informe um ID válido')
  parser.add_argument('description', type=str, required=True, help='Informe uma descrição válida')
  parser.add_argument('price', type=float, required=True, help='Informe um preço válido')

  def get(self, id):
    for po in purchase_orders:
      if po['id'] == id:
        return jsonify(po['items'])
    
    return make_response(jsonify({'message': 'Pedido de id {} não encontrado'.format(id)}), 404)
  
  def post(self, id):
    data = PurchaseOrdersItems.parser.parse_args()

    purchase_order_item = {
      'id': data['id'],
      'description': data['description'],
      'price': data['price']
    }

    for po in purchase_orders:
      if po['id'] == id:
        po['items'].append(purchase_order_item)
        return jsonify(purchase_order_item)

    return make_response(jsonify({'message':  'Pedido de id {} não encontrado'.format(id)}), 404)