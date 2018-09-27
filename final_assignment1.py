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

    print(prijs)


ritprijs(14, True, 420)




