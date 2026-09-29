import pytest
from python_examples.core_unit.pricing import final_price, shipping_cost


@pytest.mark.unit
@pytest.mark.parametrize(
    "subtotal,member,expected",
    [
        (50, False, 50.00),
        (50, True, 50.00),
        (100, True, 90.00),
        (125.50, True, 112.95),
    ],
)
def test_final_price_examples(subtotal, member, expected):
    assert final_price(subtotal, member) == expected


@pytest.mark.unit
def test_negative_subtotal_is_rejected():
    with pytest.raises(ValueError):
        final_price(-1)


@pytest.mark.unit
@pytest.mark.parametrize("subtotal,expected", [(74.99, 7.99), (75, 0.0)])
def test_shipping_boundary(subtotal, expected):
    assert shipping_cost(subtotal) == expected
