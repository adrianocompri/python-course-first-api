from flask import Flask
from flask_restful import Api
from db import db

from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems

first_time = True


def create_app():

  app = Flask(__name__)
  api = Api(app)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/python_course'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  api.add_resource(PurchaseOrders, '/purchase_orders')
  api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')
  api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

  @app.before_request
  def run_once():
    global first_time
    if first_time:
      first_time = False
      with app.app_context():
        db.create_all()

  return app