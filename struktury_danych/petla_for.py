
# ZADANIE: WYPISZ ILE JEST DANYCH ELEMNTOW (UJEMNYCH I DODATNICH0

# lista = [1,2,-3,4,5,6,-7,8,9]
#
# ile_d=0
# ile_u=0
#
# for i in lista:
#     if i >0:   # widze liczbe dodatnia
#         ile_d +=1   # zwiekszam licznik dodatnich       ile jest elementów
#
# for i in lista:
#     if i <0:   # widze liczbe ujemnych
#         ile_u +=1   # zwiekszam licznik dodatnich
#
# print(f'Na liscie jest {ile_d} liczb dodatnich')
# print(f'Na liscie jest {ile_u} liczb ujemnych')


# minusy =lista.count(1)
# print(minusy)

ile_podz =0

for i in range(101):
    if i % 3 == 0 or i % 5 ==0:
       #ile_podz += 1
        print(i)
        ile_podz += 1
print(ile_podz)