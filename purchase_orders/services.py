from .model import PurchaseOrderModel
from flask import make_response, jsonify
from .exceptions import QuantityException

class PurchaseOrdersService:

  def _check_quantity(self, quantity):
    if not (quantity >= 50 and quantity <= 150):
      raise QuantityException("A quantidade incorreta")

  def find_all(self):
    purchase_orders = PurchaseOrderModel.find_all()
    return [p.as_dict() for p in purchase_orders]
  
  def create(self, **kwargs):
    self._check_quantity(kwargs['quantity'])

    purchase_order = PurchaseOrderModel(**kwargs)
    purchase_order.save()

    return purchase_order.as_dict()
  
  def find_by_id(self, id):
    purchase_order = PurchaseOrderModel.find_by_id(id)

    if purchase_order:
      return purchase_order.as_dict()

    return make_response(jsonify({'message': 'Pedido de id {} não encontrado'.format(id)}), 404)