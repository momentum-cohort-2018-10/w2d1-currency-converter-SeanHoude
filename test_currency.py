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


def test_convert():
    assert convert(1, "USD", "USD") == 1
    assert convert(1, "USD", "EUR") == 0.877
    assert round(convert(3, "USD", "EUR"), 3) == 2.631


# (_from, to, value) = rates[0]

# print(rates[0])
# print(_from)