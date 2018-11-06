from currency import convert
import pytest

rates = [
    ('USD', 'JPY', 113.215),
    ('USD', 'CAD', 1.310),
    ('EUR', 'JPY', 129.027),
    ('USD', 'EUR', 0.877),
    ('EUR', 'CAD', 1.492),
    ('CAD', 'JPY', 86.404)
]


def test_same_currency_doesnt_change_value():
    assert convert(1, "USD", "USD") == 1

def test_dollar_changes_correctly_to_euro():
    assert round(convert(1, "USD", "EUR"), 3) == 0.877

def test_non_dollar_amt_changes_correctly():
    assert round(convert(3, "USD", "EUR"), 3) == 2.631

def test_euro_to_usd():
    assert round(convert(1, "EUR", "USD"), 3) == 1.14

def test_conversion_works_both_ways():
    assert round(convert(1, "USD", "EUR"), 3) == .877
    assert round(convert(1, "EUR", "USD"), 2) == 1.14
    assert round(convert(1, "EUR", "JPY"), 3) == 129.027
    assert round(convert(1, "JPY", "EUR"), 5) == .00775

def test_raise_value_error_if_unknown_currency():
    with pytest.raises(ValueError):
        convert(1, "KOR", "EUR")
