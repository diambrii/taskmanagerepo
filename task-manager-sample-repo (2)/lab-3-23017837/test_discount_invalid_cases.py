import pytest
from app.tasks import calculate_discount


@pytest.mark.parametrize(
    "price, premium, expected",
    [
        (-0.01, True, -0.008),
        (-0.01, False, -0.01),
        (100, "yes", 100),
        (100, 1, 80),
        (100, None, 100),
        ("invalid", False, "invalid"),
    ],
)
def test_invalid_input_behaviour(price, premium, expected):
    result = calculate_discount(price, premium)
    assert result == expected


@pytest.mark.parametrize(
    "price",
    ["invalid", None],
)
def test_invalid_price_with_premium(price):
    with pytest.raises(TypeError):
        calculate_discount(price, True)