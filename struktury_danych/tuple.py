#tupla (krotka)
#uporzadkowany ciag wartosci

# para = (1,2)
# trojka = ('ala', 'ola', 'basia')
# czworka = (1, 'pies', (12,12),2.5)
#
#
# print(para, trojka, czworka)
#
# print(czworka[2])
# print(len(trojka))
# print(czworka[1:2])
# print(trojka[1:])  #do konca
# print(czworka[:3])  #od poczatku
#
# print(czworka[-1])  #ostatni element
# print(czworka[-3:-1])
# print(czworka[::2]) # skacze co 2
# print(czworka[::-1]) - w odwrotnej kolejnosci

abc = (1,2,3,4,5,6,7,8,9,10)

print(abc[1])
print(abc[-2])
print(abc[2:7])
print(abc[::3])
print(abc[::-2])

if 4 in abc:
    print('jest  w tupli')
else:
    print('nie ma w tupli')

if 14 in abc:
    print('jest')
else:
    print('nie ma')


