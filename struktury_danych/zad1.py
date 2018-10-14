pusta_lista = []


while len(pusta_lista)<10:

    a= int(input("Podaj liczbe "))
    if a == '':
        break
    pusta_lista.append(a)
    #print(pusta_lista)

print(pusta_lista)
print('srednia',sum(pusta_lista)/len(pusta_lista))

#pusta_lista.append(a)

# while len(pusta_lista) < 10:
#     pusta_lista.append(a)
