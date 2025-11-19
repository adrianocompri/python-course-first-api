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