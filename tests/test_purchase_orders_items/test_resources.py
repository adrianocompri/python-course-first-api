import json


def test_get_items_by_purchase_order_id(test_client, seed_db):
  response = test_client.get(f'/purchase_orders/{seed_db['purchase_order'].id}/items')

  assert response.status_code == 200
  assert len(response.json) == 1

  if response.json == 1:
    assert response.json[0]['id'] == seed_db['item'].id
    assert response.json[0]['description'] == seed_db['item'].description
    assert response.json[0]['price'] == seed_db['item'].price


def test_get_items_by_purchase_order_id_not_found(test_client):
  id = 0
  response = test_client.get('/purchase_orders/{}/items'.format(id))

  assert response.status_code == 404
  assert response.json['message'] == 'Pedido de id {} não encontrado'.format(id)


def test_post_items_by_purchase_order_id(test_client, seed_db):
  obj = {
    'description': 'Item teste',
    'price': 15.99
  }
  
  response = test_client.post(
    f'/purchase_orders/{seed_db['purchase_order'].id}/items',
    data=json.dumps(obj),
    content_type='application/json'
  )

  assert response.status_code == 200
  assert response.json['id'] is not None
  assert response.json['description'] == obj['description']
  assert response.json['price'] == obj['price']


def test_post_items_by_purchase_order_id_not_found(test_client):
  id = 9999

  response = test_client.post(
    '/purchase_orders/{}/items'.format(id),
    data=json.dumps({
      'id': 2,
      'description': 'Items nro 2',
      'price': 15.99
    }),
    content_type='application/json'
  )

  assert response.status_code == 404
  assert response.json['message'] == 'Pedido de id {} não encontrado'.format(id)


def test_post_items_invalid_description(test_client, seed_db):
  response = test_client.post(
    '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
    data=json.dumps({
      'price': 15.99
    }),
    content_type='application/json'
  )

  assert response.status_code == 400
  assert response.json['message']['description'] == 'Informe uma descrição válida'


def test_post_items_invalid_price(test_client, seed_db):
  response = test_client.post(
    '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
    data=json.dumps({
      'description': 'Items nro 2'
    }),
    content_type='application/json'
  )

  assert response.status_code == 400
  assert response.json['message']['price'] == 'Informe um preço válido'