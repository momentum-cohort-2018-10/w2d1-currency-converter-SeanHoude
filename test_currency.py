from currency import convert

rates = [
    ('EUR', 'USD', 1.13966),
    ('USD', 'JPY', 113.215),
    ('USD', 'CAD', 1.31003),
    ('EUR', 'JPY', 129.027), 
    ('USD', 'EUR', 0.877),
    ('JPY', 'USD', 0.00883),
    ('CAD', 'USD', 0.763),
    ('EUR', 'CAD', 1.492),
    ('JPY', 'CAD', 0.0115),
    ('JPY', 'EUR', 0.00775),
    ('CAD', 'EUR', 0.66987),
    ('CAD', 'JPY', 86.404)
]


def test_same_currency_doesnt_change_value():
    assert convert(1, "USD", "USD") == 1

def test_dollar_changes_correctly_to_euro():
    assert round(convert(1, "USD", "EUR"), 3) == 0.877

def test_non_dollar_amt_changes_correctly():
    assert round(convert(3, "USD", "EUR"), 3) == 2.631

def test_conversion_works_both_ways():
    assert round(convert(3, "USD", "CAD"), 3) == 3.93
    assert round(convert(3, "CAD", "USD"), 2) == 2.29
