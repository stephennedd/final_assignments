stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
def inlezen_beginstation(stations):

    while True:
        fout = 'De gegeven station is niet van toepassing'
        beginstation = input('Wat is je beginstation?: ')
        if beginstation == 'Maastricht':
            print(fout)
            continue
        if beginstation in stations:
            return beginstation
        else:
            print(fout)

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Wat is je eindstation?: ')

        fout = 'De station ' + eindstation + ' is niet van toepassing.'

        if eindstation in stations and stations.index(eindstation) >= stations.index(beginstation) and beginstation != eindstation:
            return eindstation
        print(fout)


def omproepen_reis(stations, beginstation, eindstation):
    station_lijst = stations[stations.index(beginstation) + 1:stations.index(eindstation)]
    aantalhaltes = stations.index(eindstation)-stations.index(beginstation)
    print('Het beginstation', ' ', beginstation, ' ', 'is het', ' ', stations.index(beginstation), 'e station in het traject.', sep='')
    print('Het eindstation', ' ', eindstation, ' ', 'is het', ' ', stations.index(eindstation), 'e station in het traject.', sep='')
    print('De afstand bedraagt', aantalhaltes, 'station(s).')
    print('De prijs van het kaartje is', aantalhaltes * 5, 'Euro(s)')
    print('')
    print('Jij stapt in de trein in: ', beginstation)
    for station in station_lijst:
        print('-', station, end='\n')
    print('Jij stapt uit in: ', eindstation)

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omproepen_reis(stations,beginstation,eindstation)