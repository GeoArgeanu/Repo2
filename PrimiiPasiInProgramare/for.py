# 101 dalmatieni
for i in range(1, 102):
    print(f'Dalmatianul cu nr {i}')

# pas din 2 in 2
# for i in range (1, 102, 2)

numere = [3, 7, 10, 20, 30]
# parcurgem lista cu for prin intermediul indexului
for i in range(0, len(numere)):
    print(f'indexul curent este {i}')
    print(f'numarul curent este {numere[i]}')

# for each
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
print(f'Suma este {s}')    