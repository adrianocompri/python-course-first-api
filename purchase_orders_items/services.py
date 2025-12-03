from flask import make_response, jsonify
from purchase_orders.model import PurchaseOrderModel
from .model import PurchaseOrdersItemsModel


class PurchaseOrdersItemsService:

  def find_by_purchase_order_id(self, id):
    purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(id)
    
    if purchase_orders_items:
      return [p.as_dict() for p in purchase_orders_items]

    return make_response(jsonify({'message': 'Pedido de id {} não encontrado'.format(id)}), 404)
  
  def create(self, **kwargs):
    purchase_order = PurchaseOrderModel.find_by_id(kwargs['purchase_order_id'])

    if not purchase_order:
      return make_response(jsonify({'message':  'Pedido de id {} não encontrado'.format(kwargs['purchase_order_id'])}), 404)
    
    purchase_order_item = PurchaseOrdersItemsModel(**kwargs)
    purchase_order_item.save()

    return purchase_order_item.as_dict()