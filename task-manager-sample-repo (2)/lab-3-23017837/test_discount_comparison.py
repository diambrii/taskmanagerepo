import pytest

from app.tasks import calculate_discount


@pytest.mark.parametrize(
    "price,is_premium,expected",
    [
        (0, True, 0),
        (0, False, 0),
        (0.01, True, 0.008),
        (0.01, False, 0.01),
        (25, True, 20),
        (25, False, 25),
        (49.99, True, 39.992),
        (49.99, False, 49.99),
        (250, True, 200),
        (250, False, 250),
    ],
    ids=[
        "TC01_zero_premium",
        "TC02_zero_regular",
        "TC03_min_positive_premium",
        "TC04_min_positive_regular",
        "TC05_ordinary_premium",
        "TC06_ordinary_regular",
        "TC07_decimal_premium",
        "TC08_decimal_regular",
        "TC09_higher_premium",
        "TC10_higher_regular",
    ],
)
def test_discount_comparison(price, is_premium, expected):
    """Check the discount for selected valid prices and both membership statuses."""
    assert calculate_discount(price, is_premium) == pytest.approx(expected)
