"""
Quest: z dict trzeba wybrac tylko elementy o danych parametrach
"""

# kind of inventory
h = {
    'h1': {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'd': 'D',
    },
    'h2': {
        'a': 'A',
        'b': 'B',
        'c': 'CC',
        'd': 'D',
    },
    'h3': {
        'a': 'A',
        'b': 'BB',
        'c': 'C',
        'd': 'DD',
    },
}

# Funkcja all way


def abla(host, **kwargs):
    # iteruj po wszystkich w dict h
    filtered = {}
    for n, h in host.items():
        # dopisz do wyniku
        filtered[n] = h
        # iteruj po ograniczeniach
        for k, v in kwargs.items():
                # sprawdzaj warunki i jesli warunek nie jest spelniony to wyrzuc z tablicy wyniku i przestan iterowac po warunkach
            if h.get(k) != v:
                filtered.pop(n)
                break
    return filtered


def abla2(hosts, **kwargs):
    filtered = {
        n: h
        for n, h in hosts.items()
        if all(h.get(k) == v for k, v in kwargs.items())
    }
    return filtered


print(abla(h, a='A', b='B', d='D'))
print(abla(h, c='CC'))
print('---------------------------')
print(abla2(h, a='A', b='B', d='D'))
print(abla2(h, c='CC'))
print('The same results')