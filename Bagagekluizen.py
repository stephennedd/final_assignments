def optieKiezen():
    a = '1: Ik wil weten hoeveel kluizen nog vrij zijn'
    b = '2: Ik wil een nieuwe kluis'
    c = '3: Ik wil even iets uit mijn kluis halen'
    print('', a, '\n', b, '\n', c, '\n')
    keuze = int(input('Voor welke optie kies je? 1, 2 of 3: '))
    if keuze == 1:
        toon_aantal_kluizen_vrij()
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_openen()
    else:
        print('Foutmelding!')


def toon_aantal_kluizen_vrij():
    kluizen_read = open("kluizen.txt", "r+")
    bezet = 0

    for line in kluizen_read.readlines():
        bezet += 1

    print('Er zijn ', 12 - bezet, ' kluizen vrij.\n')
    kluizen_read.close()


def nieuwe_kluis():
    kluisnummers = list(range(1, 13))
    bezet = 0

    if bezet < 12:
        kluizen_read = open("kluizen.txt", 'r+')

        for item in kluizen_read:
            kluisnummer = int(item[0])
            if kluisnummer in kluisnummers:
                kluisnummers.remove(kluisnummer)

        kluizen_read.close()

        code = input('Vul een passend code in: ')

        kluizen_append = open("kluizen.txt", "a")
        kluizen_append.write(str(min(kluisnummers)) + ';'+ str(code) + '\n')
        print('Uw kluisnummer is: ' , min(kluisnummers), ' en uw code is: ' , code, '\n')

    else:
        print('Geen kluizen meer beschikbaar!')

    kluizen_append.close()


def kluis_openen():
    bezet = 0

    if bezet < 12:
        lines = open("kluizen.txt", "r")

        kluis_input = (input('Geef uw kluisnummer:'))
        code_input = (input('Geef uw code:'))

        i = False

        for x in lines:
            lines_split = x.split(";")
            kluisnummer = lines_split[0]
            code = lines_split[1].strip()
            if kluis_input == kluisnummer and code_input == code:
                i = True

        if i:
            print('Uw kluis is open!')
        else:
            print('Er is een fout in uw gegevens!')
        kluizen_read.close()

optieKiezen()

