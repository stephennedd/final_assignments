def standaardprijs(AfstandKM):
    afstand = float(input('Enter the distance in KM to your destination: '))
    prijs = float(afstand * 0.80)
    if afstand >= 50:
        prijs = int(15) + (afstand*0.60)
        print(prijs)
    elif afstand <= int(0):
        prijs = float(0.00)
    print('The price of the journey is €',"%.2f" % round(prijs,2))
standaardprijs(1)

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(1)
    weekendrit = bool
