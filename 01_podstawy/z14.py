# kommenda koncowa --> stop
# jesli uzytkownik nie wpisze zadnej liczby --> wypisujemy "brak danych"

# 3 znmienne do przechowywania danych
# min_1 =  0
# max_1 =  0
# #akt_1 =




odp= input('wpisz liczbe lub "stop"')
if odp.strip('"') == 'stop':
    print('brak danych')


else:
    akt_1 = int(odp)
    min_1 = int(odp)
    max_1 = int(odp)
    while odp!= 'stop':
        akt_1 = int(odp)
        if akt_1 > max_1:
            max_1 = akt_1

        if akt_1 < min_1:
            min_1 = akt_1

        odp= input('wpisz liczbe lub "stop"')
        print(f'najwieksza znalezniona: {max_1}\n'
              f'najmnijsza znalezniona: {min_1}')



#    tu jest miejsce na obsluge tego co uzytkonik nam dal
#   akt_1= int(odp)
#     if akt_1 > max_1:
# #        max_1 = akt_1
# print (f'najwieksza znalezniona: {max_1}')