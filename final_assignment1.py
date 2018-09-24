def standaardprijs(AfstandKM):
    afstand = int(input('Enter the distance in KM to your destination: '))
    prijs = afstand * 0.80
    if afstand >= 50:
        prijs = int(15) + (afstand*0.60)
        print(prijs)
    elif afstand <= int(0):
        prijs = float(0.00)
    print('The price of the ride is €',prijs)
standaardprijs('a')

