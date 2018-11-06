rates = [
    ('USD', 'JPY', 113.215),
    ('USD', 'CAD', 1.310),
    ('EUR', 'JPY', 129.027),
    ('USD', 'EUR', 0.877),
    ('EUR', 'CAD', 1.492),
    ('CAD', 'JPY', 86.404)
]


def convert(value, original, to):
    if original == to:
        return value
    else:
        for tup in rates:
            if original in tup and to in tup:
                if original == tup[0]:
                    return value * tup[2]
                if original == tup[1]:
                    return value / tup[2]
    raise ValueError(F"Can't convert from {original} to {to}.")
