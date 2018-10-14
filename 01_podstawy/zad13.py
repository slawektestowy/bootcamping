#zbieranie danych czastkowych
# najpierw przygotowujemy pusty kubelek

kubelek = 0

# w kazdym obrocie petli do kubelka dodaje
# kolejne liczby

# rozwiazanie z petla
nr_dnia= 1
ile_dni =7
suma_temp = 0
while nr_dnia <= ile_dni:
    suma_temp += int(input(f'podaj temp {nr_dnia}.dzien'))
    nr_dnia += 1
print(f'srednia temp to {suma_temp/ile_dni:.2f}')

# p = float(input("Podaj temperture  w poniedzialek: "))
# w = float(input("Podaj tem we wtorek: "))
# s = float(input("Podaj temp w srode: "))
# c = float(input("Podaj temp w czwarte: "))
# p = float(input("Podaj temp w piatek: "))
# so = float(input("Podaj temp w sobote: "))
# nie = float(input("Podaj temp w sobote: "))
#
# prognoza1 = p + w + s + c + p + so + nie


