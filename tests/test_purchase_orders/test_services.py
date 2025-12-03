import pytest

from purchase_orders.services import PurchaseOrdersService
from purchase_orders.exceptions import QuantityException


@pytest.mark.nocleardb
def test_check_quantity_less_then_minimun():
  with pytest.raises(QuantityException) as ex:
    PurchaseOrdersService()._check_quantity(49)

  assert ex.value.code == 400
  assert ex.value.description == 'A quantidade incorreta'

@pytest.mark.nocleardb
def test_check_quantity_greatest_then_maximum():
  with pytest.raises(QuantityException) as ex:
    PurchaseOrdersService()._check_quantity(151)

  assert ex.value.code == 400
  assert ex.value.description == 'A quantidade incorreta'
