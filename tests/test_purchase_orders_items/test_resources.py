import json


def test_get_items_by_purchase_order_id(test_client):
  response = test_client.get('/purchase_orders/1/items')

  assert response.status_code == 200
  assert len(response.json) == 1

  if response.json == 1:
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'Items nro 1'
    assert response.json[0]['price'] == 19.99


def test_get_items_by_purchase_order_id_not_found(test_client):
  id = 9999
  response = test_client.get('/purchase_orders/{}/items'.format(id))

  assert response.status_code == 404
  assert response.json['message'] == 'Pedido de id {} não encontrado'.format(id)


def test_post_items_by_purchase_order_id(test_client):
  response = test_client.post(
    '/purchase_orders/1/items',
    data=json.dumps({
      'id': 2,
      'description': 'Items nro 2',
      'price': 15.99
    }),
    content_type='application/json'
  )

  assert response.status_code == 200
  assert response.json['id'] == 2
  assert response.json['description'] == 'Items nro 2'
  assert response.json['price'] == 15.99


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