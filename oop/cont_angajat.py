class Angajat:
    # constructor
    def __init__(self, nume, prenume, salariu, vechime):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.calificare = 'Programator'
        self.vechime = vechime

    def descriere(self):
        print(f'Numele angajatului este {self.nume} {self.prenume}')
        print(f'Functia este de {self.calificare}')
        print(f'Vechimea este de {self.vechime} ani')
        print(f'Salariul este de {self.salariu} lei')

    def marire_salariu(self):
        if self.vechime <= 5:
            print('Marirea salariala va fi de 300 lei')
            print(f'Totalul este de {self.salariu + 300}')
        elif 5 <= self.vechime <= 10:
            print('Marirea salariala va fi de 500 de lei')
            print(f'Totalul este de {self.salariu + 500}')
        else:
            print('Marirea salariala va fi de 700 de lei')
            print(f'Totalul este de {self.salariu + 700}')
        print('----------------------------------')


    # def actualizare_valori(self):
    #     self.vechime = noua_vechime
    #     self.noua_vechime = self.vechime + 1
    #     #self.noua_vechime +=1 self.vechime



cont1 = Angajat('Geo', 'Argeanu', 1500, 7)
cont2 = Angajat('Andrei', 'Argeanu', 1000, 5)
cont3 = Angajat('Alex', 'Argeanu', 2000, 15)

cont1.descriere()
cont1.marire_salariu()

cont2.descriere()
cont2.marire_salariu()

cont3.descriere()
cont3.marire_salariu()

