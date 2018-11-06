rates = [
    # ('USD', 'JPY', 113.215),
    ('USD', 'CAD', 1.310),
    ('EUR', 'JPY', 129.027),
    ('USD', 'EUR', 0.877),
    ('EUR', 'CAD', 1.492),
    ('CAD', 'JPY', 86.404)
]


def convert(value, original, to):
    if original == to:
        return value

    direct = [tup for tup in rates if original in tup and to in tup]
    forward = [tup for tup in rates if original in tup[0] and to not in tup[1]]
    reverse = [tup for tup in rates if original in tup[1] and to not in tup[0]]
    # original_exists = [tup for tup in rates if original in tup]
    # to_exists = [tup for tup in rates if to in tup]

    # if not original_exists and not to_exists:
        
    if direct:
        if original == direct[0][0]:
            return value * direct[0][2]
        if original == direct[0][1]:
            return value / direct[0][2]
    if forward:
        midway_currency = forward[0][1]
        midway_rate = forward[0][2]
        final = [tup for tup in rates if midway_currency in tup[0] and to in tup[1]]
        return value * midway_rate * final[0][2]
    if reverse:
        midway_currency = reverse[0][0]
        midway_rate = reverse[0][2]
        final = [tup for tup in rates if midway_currency in tup[1] and to in tup[0]]
        return value / midway_rate / final[0][2]
    raise ValueError(F"Can't convert from {original} to {to}.")

# print(convert(1, 'KOR', 'JPY'))