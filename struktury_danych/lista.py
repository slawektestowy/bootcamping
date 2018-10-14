#listy to uporzadkowane ciagi elementów

lista = [1,2,3,4,1]

print(lista[1])
print(lista[-1:-5:-2])

lista.append(6)
print(lista)
print(lista.count(1))

#lista.insert(2,'ala ma kota') #wstawienie w miejsce 2
print(lista)


del lista[5]  #usuniecie elementu na pozycji 5
print(lista)
lista.remove(1) #usuniecie PIERWSZEGO konretnego elemntu , w tym wyapdku dwojka (tylko 1)
print(lista)

lista.sort()
print(lista)