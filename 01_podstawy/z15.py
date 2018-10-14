#plansza id 1 do 10
from random import random


#przygotowanie planszy
gracz_x = int(random() *10) + 1  # ctrl + q --> opis funkcji
gracz_y = int(random() *10) + 1

print(f'pozycja gracza: ({gracz_x}, {gracz_y})')



skarb_x = int(random() *10) + 1  # ctrl + q --> opis funkcji
skarb_y = int(random() *10) + 1

poz_gracza = gracz_x, gracz_y
poz_skarbu = skarb_x, skarb_y
#print(f'test pozycji racza {poz_gracza}')
#print(f'test pozycji skarbu {poz_skarbu}')


while True:
    print(f'pozycja gracza: ({gracz_x}, {gracz_y})')

    odleglosc_poprzednia = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    ruch = input("podaj kierunke ruchu [p l g d]:")

    if ruch =='p':
        gracz_x +=1
    elif ruch == "l":
        gracz_x -=1
    elif ruch == 'g':
        gracz_y +=1
    elif ruch == 'd':
        gracz_y -=1
    else:
        break

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('Masz skarb!!')

    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print("Spadleś z plansz, KONIEC GRY")

    odleglosc_po_ruchu = abs(gracz_x-skarb_x) + abs(gracz_y - skarb_y)
    if odleglosc_poprzednia > odleglosc_po_ruchu:
        print('cieplo')
    else:
        print('zimno')




    # if poz_gracza == poz_skarbu:
    #          print("Dotales do skarbu")
    #          exit(0)

    # if gracz_x == skarb_x and gracz_y == skarb_y:
    #     print('Masz skarb!!')
    #

     # elif poz_gracza > poz_skarbu:
     #         print("daleko")

