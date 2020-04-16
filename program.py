# GRA W WISIELCA

import time
import random
import os


def WyswietlElementyLIstyWLini(lista):
    bufor = ''
    for litera in lista:
        bufor += litera
    return bufor


listaWyrazow = ['abecadło', 'portmonetka', 'konduktor', 'żółw', 'fatamorgana', 'oneironautyka', 'majster', 'kołnierzyk', 'zawadiaka', 'złotousty', 'magnetofon', 'klawikord', 'essej', 'melancholia']

przerwa = 0.7

while True:
    os.system('cls')
    print('*** GRA WISIELEC ***\n')
    print('1 <- Nowa gra')
    print('2 <- Lista słówek')
    print('E <- Wyjście z programu\n')

    opcja = input('Którą opcję chcesz wybrać?')

    if opcja == '1':

        wyrazDoOdgadniecia =[litera for litera in random.choice(listaWyrazow)]
        wyrazAktualny = ['-' for litera in wyrazDoOdgadniecia]




        licznik = 0

        while wyrazDoOdgadniecia != wyrazAktualny and licznik < 10:

            
            os.system('cls')

            print('*** GRA WISIELEC ***\n')
            print('Zgadnij ukryte słowo:\n')
            print(WyswietlElementyLIstyWLini(wyrazAktualny) + '\n')
            print('Licznik pudeł:', licznik)

            litera = (input('Podaj literę:'))[0]


            if litera in wyrazAktualny and litera in wyrazDoOdgadniecia:
                licznik += 1
                print('Podałeś już tą literę wcześniej!')
                time.sleep(przerwa)
                continue
            elif litera in wyrazDoOdgadniecia and not (litera in wyrazAktualny):
                print('Brawo, trafiłeś tą literę!')
                time.sleep(przerwa)
                for x in range(0, wyrazDoOdgadniecia.count(litera)):
                        for i in range(0, len(wyrazDoOdgadniecia)):
                            if litera == wyrazDoOdgadniecia[i]:
                                wyrazAktualny[i] = litera        
                
            else:
                print('Podanej litery nie ma w tym wyrazie.')
                time.sleep(przerwa)
                licznik += 1

        if licznik == 10:
            os.system('cls')
            print('*** GRA WISIELEC ***\n')
            print('Niestety, przegrałeś, za dużo pudeł.\n')
            print('Ukryty wyraz to:' + WyswietlElementyLIstyWLini(wyrazDoOdgadniecia))
        else:
            os.system('cls')
            print('*** GRA WISIELEC ***\n')
            print('Brawo, zgadłeś po ' + str(licznik) + ' pudłach!')
        
        time.sleep(przerwa * 3)
    
    elif opcja == '2':

        os.system('cls')   
        print('*** GRA WISIELEC ***\n')
        print('Lista wyrazów w bazie:\n')

        for wyraz in listaWyrazow:
            print(wyraz)
        
        input('\nWciśnij dowolny znak i Enter:')
    else:
        break