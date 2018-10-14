
# from random import random

from random import random




x= random() *100 //1
x =round(random() *100,0)
print(x)
y= random() *100 //1
y =round(random() *100,0)
print(y)

if 0 <= x <=10:
    if 0 <= y <=10:
        print("kom1")
    elif 10 <= y <=90:
        print("kom2")
    elif 90 <= y <=100:
        print("kom3")
    else:
        print("jestes poza plansza")
elif 10 <= x <= 90:
    if 0 <= y <=10:
        print("kom3")
    elif 10 <= y <=90:
        print("kom5")
    elif 90 <= y <=100:
        print("kom6")
    else:
        print("jestes poza plansza")
elif 90 <= x <= 100:
    if 0 <= y <=10:
        print("kom7")
    elif 10 <= y <=90:
        print("kom8")
    elif 90 <= y <=100:
        print("kom9")
    else:
        print("jestes poza plansza")
else:
    print("jestes poza plansza")