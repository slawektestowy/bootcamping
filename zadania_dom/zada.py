# UWAGA: zadanie domowe:
# wylosuj liczbę z zakresu 0-100
# poproś użytkownika żeby zgadł co to za liczba
# jeśli użytkownik nie zgadnie to podpowiedz mu "za dużo" / "za mało"
# powtarzaj aż użytkownik zgadnie (lub przerwie zabawę)
# na koniec wyświetl ile prób potrzebował, żeby zgadnąć
import random

a = range(100)
b = random.choice(a)
print(b)

c = int(input("Podaj liczbe: "))
t = 0
g = 0
for z in a:
    if c > b:
        print("za duzo")
        c = int(input("Podaj liczbe: "))
        t +=1
    if c < b:
        print ("za malo")
        c = int(input("Podaj liczbe: "))
        g +=1
    if c == b:
        print(f'Udało sie za {t+g+1} razem')
        break






# while c == b:
#     print("TAAAK")
#     continue
# while c > b:
#     print("za duzo")
#     c = int(input("Podaj liczbe: "))
#     continue
#     while c < b:
#         print("za malo")
#         c = int(input("Podaj liczbe: "))
#         continue
#
# if c == b:
#     print("Udało sie")
# elif c > b:
#     print("Za duzo")
# elif c < b:
#     print("za malo")
