rates = [('EUR', 'USD', 1.13966), ('USD', 'JPY', 113.215), ('USD', 'CAD', 1.31003), ('EUR', 'JPY', 129.027), 
('USD', 'EUR', 0.877), ('JPY', 'USD', 0.00883), ('CAD', 'USD', 0.763), ('EUR', 'CAD', 1.492), ('JPY', 'CAD', 0.0115),
('JPY', 'EUR', 0.00775), ('CAD', 'EUR', 0.66987), ('CAD', 'JPY', 86.404)]


def convert(_value, _from, _to):
    if _from == _to:
        return _value
    else:
        for tup in rates:
            if tup[0] == _from:
                if tup[1] == _to:
                    rate = tup[2]
        return _value * rate