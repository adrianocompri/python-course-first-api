from flask import jsonify
from flask_restful import Resource, reqparse
from purchase_orders.resources import purchase_orders


class PurchaseOrdersItems(Resource):

  parser = reqparse.RequestParser()

  parser.add_argument('id', type=int, required=True, help="Informe um id")
  parser.add_argument('description', type=str, required=True, help="Informe uma descricao")
  parser.add_argument('price', type=float, required=True, help="Informe um valor")

  def get(self, id):
    for po in purchase_orders:
      if po['id'] == id:
        return jsonify(po['items'])
      
    return jsonify({'message': f'Itens do pedido {id} não foi encontrado'})
  
  def post(self, id):
    request_data = PurchaseOrdersItems().parser.parse_args()

    for po in purchase_orders:

      if po['id'] == id:
        
        po['items'].append({
          "id": request_data['id'],
          "description": request_data['description'],
          "price": request_data["price"]
        })

        return jsonify(po['items'])
      
    return jsonify({'message': f'Itens do pedido {id} não foi encontrado'})