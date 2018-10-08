def standaardprijs(afstandKM):
    prijs = afstandKM * 0.80
    if afstandKM >= 50:
        prijs = 15 + (afstandKM - 50)*0.60
    elif afstandKM < 0:
        prijs = 0.00
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)

    if weekendrit and (leeftijd < 12 or leeftijd >= 65):
        prijs = prijs / 100 * 65
    elif weekendrit:
        prijs = prijs / 100 * 60
    elif leeftijd < 12 or leeftijd >= 65:
        prijs = prijs / 100 * 70
    return prijs

def testwaardes():
    a = 'De weekend ritprijs op leeftijd van 11 en afstand van 1km: '
    b = 'De weekend ritprijs op leeftijd van 11 en afstand van 100km: '
    c = 'De weekend ritprijs op leeftijd van 11 en afstand van -1: '
    print(a, ritprijs(11, True, 1))
    print(b, ritprijs(11, True, 100))
    print(c, ritprijs(11, True, -1))
    print(' ')

    d = 'De week ritprijs met leeftijd van 11 en afstand van 1km: '
    e = 'De week ritprijs met leeftijd van 11 en afstand van 100km:'
    f = 'De week ritprijs met leeftijd van 11 en afstand van -1:'
    print(d, ritprijs(11, False, 1))
    print(e, ritprijs(11, False, 100))
    print(f, ritprijs(11, False, -1))
    print(' ')

    g = 'De weekend ritprijs met leeftijd van 12 en afstand van 1km: '
    h = 'De weekend ritprijs met leeftijd van 12 en afstand van 100km: '
    i = 'De weekend ritprijs met leeftijd van 12 en afstand van -1km: '
    print(g, ritprijs(12, True, 1))
    print(h, ritprijs(12, True, 100))
    print(i, ritprijs(12, True, -1))
    print(' ')

    j = 'De week ritprijs met leeftijd van 12 en afstand van 1 km: '
    k = 'De week ritprijs met leeftijd van 12 en afstand van 100 km: '
    l = 'De week ritprijs met leeftijd van 12 en afstand van -1 km: '
    print(j, ritprijs(12, False, 1))
    print(k, ritprijs(12, False, 100))
    print(l, ritprijs(12, False,-1))
    print(' ')

    m = 'De weekend ritprijs met leeftijd van 64 en afstand van 1 km: '
    n = 'De weekend ritprijs met leeftijd van 64 en afstand van 100 km: '
    o = 'De weekend ritprijs met leeftijd van 64 en afstand van -1 km: '
    print(m, ritprijs(64, True, 1))
    print(n, ritprijs(64, True, 100))
    print(o, ritprijs(64, True, -1))
    print(' ')

    p = 'De week ritprijs met leeftijd van 64 en afstand van 1 km: '
    q = 'De week ritprijs met leeftijd van 64 en afstand van 100 km: '
    r = 'De week ritprijs met leeftijd van 64 en afstand van -1 km: '
    print(p, ritprijs(64, False, 1))
    print(q, ritprijs(64, False, 100))
    print(r, ritprijs(64, False, -1))
    print(' ')

    s = 'De weekend ritprijs met leeftijd van 65 en afstand van 1km: '
    t = 'De weekend ritprijs met leeftijd van 65 en afstand van 100km: '
    u = 'De weekend ritprijs met leeftijd van 65 en afstand van -1km: '
    print(s,ritprijs(65, True, 1))
    print(t,ritprijs(65, True, 100))
    print(u,ritprijs(65, True, -1))
    print(' ')

    v = 'De week ritprijs met leeftijd van 65 en afstand van 1km: '
    w = 'De week ritprijs met leeftijd van 65 en afstand van 100km: '
    x = 'De week ritprijs met leeftijd van 65 en afstand van -1km: '
    print(v, ritprijs(65, False, 1))
    print(w, ritprijs(65, False, 100))
    print(x, ritprijs(65, False, -1))
    print(' ')

testwaardes()