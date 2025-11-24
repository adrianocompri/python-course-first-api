from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from .model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel

purchase_orders = []

class PurchaseOrdersItems(Resource):
  parser = reqparse.RequestParser()

  parser.add_argument('description', type=str, required=True, help='Informe uma descrição válida')
  parser.add_argument('price', type=float, required=True, help='Informe um preço válido')

  def get(self, id):
    purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(id)
    
    if purchase_orders_items:
      return [p.as_dict() for p in purchase_orders_items]

    return make_response(jsonify({'message': 'Pedido de id {} não encontrado'.format(id)}), 404)
  
  def post(self, id):
    purchase_order = PurchaseOrderModel.find_by_id(id)

    if not purchase_order:
      return make_response(jsonify({'message':  'Pedido de id {} não encontrado'.format(id)}), 404)
    
    data = PurchaseOrdersItems.parser.parse_args()
    data['purchase_order_id'] = id

    purchase_order_item = PurchaseOrdersItemsModel(**data)
    purchase_order_item.save()

    return purchase_order_item.as_dict()