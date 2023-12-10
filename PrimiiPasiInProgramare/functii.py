def printGreeting():
    print('Buna ziua!, Bine ati venit')

def printGreetingByName ( nume, prenume ):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr (a, b, c):
    return (a + b +c)/ 3

def piValue():
    return 3.14

def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


# zona de apelare ( desktop)
printGreeting()
printGreeting()
printGreetingByName(' Argeanu ', ' Georgiana ')
printGreetingByName(' Argeanu ', ' Alexandru ')
print(mediaNr(3,3,4))
print(piValue())


# se ia varsta utilizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat bine ati venit in aplicatie')
else:
    print('Nu ai varsta minima necesara (18) pentru a paria')



