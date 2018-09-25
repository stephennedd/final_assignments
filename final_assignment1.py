def standaardprijs():
    afstand = float(input('Enter the distance in KM to your destination: '))
    prijs = afstand * 0.80
    if afstand >= 50:
        prijs = 15 + (afstand*0.60)
        print(prijs)
    elif afstand < int(0):
        prijs = float(0.00)
    print('The price of the journey is €',"%.2f" % round(prijs,2))


def ritprijs():
    standaardprijs()
    leeftijd = int(input('Please enter your age: '))
    if leeftijd < 12:

    weekendrit = str(input('Are you traveling on a weekend? True/False'))
    if weekendrit == 'True':
        weekendrit = True




ritprijs()




