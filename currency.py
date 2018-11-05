rates = [('EUR', 'USD', 1.13966), ('USD', 'JPY', 113.215), ('USD', 'CAD', 1.31003), ('EUR', 'JPY', 129.027), 
('USD', 'EUR', 0.877), ('JPY', 'USD', 0.00883), ('CAD', 'USD', 0.763), ('EUR', 'CAD', 1.492), ('JPY', 'CAD', 0.0115),
('JPY', 'EUR', 0.00775), ('CAD', 'EUR', 0.66987), ('CAD', 'JPY', 86.404)]


def convert(value, original, to):
    if original == to:
        return value
    else:
        for tup in rates:
            if original in tup and to in tup:
                if original == tup[0]:
                    return value * tup[2]
