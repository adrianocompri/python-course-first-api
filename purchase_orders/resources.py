from flask_restful import Resource, reqparse
from .services import PurchaseOrdersService


class PurchaseOrders(Resource):

  __service__ = PurchaseOrdersService()

  parser = reqparse.RequestParser()

  parser.add_argument('description', type=str, required=True, help='Informe uma deescrição válida')
  parser.add_argument('quantity', type=int, required=True, help='Informe uma quantidade válida')

  def get(self):
    return self.__service__.find_all()

  def post(self):
    data = PurchaseOrders.parser.parse_args()
    return self.__service__.create(**data)


class PurchaseOrdersById(Resource):
  __service__ = PurchaseOrdersService()

  def get(self, id):
    return self.__service__.find_by_id(id)
