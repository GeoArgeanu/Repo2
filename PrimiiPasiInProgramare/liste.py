# LSTELE POT SA CUPRINDA ELEM DE TIPURI DIFERITE
# AU DIMENSIUNE DINMICA

fructe = ['mar' , 'banana' , 'portocala' , 3 , True]

# afisam lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = ('para')
print(fructe)

# dimensiunea
print(len(fructe))

# scoate si ne da ultimulelement
last = fructe.pop()
print('ultimul element :' ,last)
print('lista :' , fructe)

# extindem lista
fructe_exotice = ['ananas' , 'kivi']
fructe.extend(fructe_exotice)
print(fructe)