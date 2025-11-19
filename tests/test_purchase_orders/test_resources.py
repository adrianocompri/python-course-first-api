import json

def test_get_purchase_orders(test_client):
  response = test_client.get('/purchase_orders')

  assert response.status_code == 200
  assert response.json[0]['id'] == 1
  assert response.json[0]['description'] == 'Pedido nro 1'


def test_post_purchase_orders(test_client):
  obj = {'id': 2, 'description': 'Pedido nro 2'}

  response = test_client.post(
    '/purchase_orders',
    data=json.dumps(obj),
    content_type='application/json'
  )

  assert response.status_code == 200
  assert response.json['id'] == obj['id']
  assert response.json['description'] == obj['description']
  assert response.json['items'] == []


def test_post_empty_id(test_client):
  response = test_client.post(
    '/purchase_orders',
    data=json.dumps({'descrition': 'Qualquer coisa'}),
    content_type='application/json'
  )

  assert response.status_code == 400
  assert response.json['message']['id'] == 'Informe um ID válido'


def test_post_empty_description(test_client):
  response = test_client.post(
    '/purchase_orders',
    data=json.dumps({'id': 3}),
    content_type='application/json'
  )

  assert response.status_code == 400
  assert response.json['message']['description'] == 'Informe uma deescrição válida'


def test_get_purchase_order_by_id(test_client):
  response = test_client.get('/purchase_orders/1')

  assert response.status_code == 200
  assert response.json['id'] == 1
  assert response.json['description'] == 'Pedido nro 1'

def test_get_purchase_order_not_found(test_client):
  id = 9999
  response = test_client.get('/purchase_orders/{}'.format(id))

  assert response.status_code == 200
  assert response.json['message'] == 'Pedido de id {} não encontrado'.format(id)