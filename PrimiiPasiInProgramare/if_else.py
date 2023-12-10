# if
# piesa_faina = True
# print('pornim radio')
# if piesa_faina == True:
#     print('dam mai tare')
#     print('fredonam')
# print('oprim radioul')

# if else
# daca nr este par printam acest lucru
# altfel printam impar

nr = -9
# ce inseamna par? se imparte la 2
# ce inseamna se imparte da 2? nu da rest 0

# if nr % 2 == 0:
#     print('nr par')
# else:
#     print('impar')
# if (nr > 0):
#     print('pozitiv')
# else:
#     print('nr nu este pozitiv')

# cum ne saluta robotul in fct de ora?
# luam date de la tastatura
# ne asguaram ca sunt transformate din string in int
# ora = int(input('Introdu ora'))
# if ora <= 0:
#     print('ora negativa')
# elif ora <= 11:
#     print('Buna dimineata')
# elif ora <= 18:
#     print('Buna ziua')
# elif ora <= 21:
#     print('Buna seara')
# elif ora <= 24:
#     print('Noapte buna')
# else:
#     print('ora mai mare de 24')

optiune = int(input('Alege o obtiune'))
if optiune == 0:
    print('Meniu anterior')
elif optiune == 1:
    print('Ati ales romana')
elif optiune == 2:
    print('Ati ales egleza')
else:
    print('mai incearca')
