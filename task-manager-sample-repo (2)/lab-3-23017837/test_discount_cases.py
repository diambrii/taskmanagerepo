import pytest
from app.tasks import calculate_discount


@pytest.mark.parametrize(
    "price, is_premium, expected",
    [
        (0, True, 0),
        (0, False, 0),
        (0.01, True, 0.008),
        (0.01, False, 0.01),
        (1, True, 0.8),
        (1, False, 1),
        (100, True, 80),
        (100, False, 100),
        (1000000, True, 800000),
        (1000000, False, 1000000),
    ],
)
def test_calculate_discount_cases(price, is_premium, expected):
    result = calculate_discount(price, is_premium)
    assert result == pytest.approx(expected)