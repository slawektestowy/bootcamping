a = int(input("podaj 1 liczbe"))
b = int(input("podaj 2 liczbe"))

o= input("podaj opercaje")
o= o.strip()

print("wynik dzialania: ", end="")
if o == "+":
    print(a+b)
elif o == "-":
    print(a-b)
elif o == "*":
    print(a*b)
elif  o == "/":
    print(a/b)
else:
    print("nie ma takiej operacji")