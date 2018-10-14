# cena_kg = 10.0
# waga= 2.5
# naleznosc = cena_kg * waga
#
# #print (f 'cena: {cena_kg}', f 'waga: {waga}', naleznosc)
#
# print(f'Cena towaru: {cena_kg}\n'
#       f'Waga: {waga}\n'
#       f'Koszt: {naleznosc}')

#input

z= int(input('wpisz liczbe'))
a= str(input('podaj swoje imie'))

aa =  input("Podaj miasto A ")
bb =  input ("Podaj miasto B ")
dystans =  int(input(f"Podaj odleglosc {aa}-{bb}: "))
cena_paliwa = float(input('Podaj cene paliwa '))
spalanie_100 = float(input("Podaj spalanie "))

print(f"Koszt przejazdu {aa}-{bb} to {dystans/100*cena_paliwa*spalanie_100:.2f}PLN")


