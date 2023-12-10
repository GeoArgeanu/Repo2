class ContBancar:
    # constructor
    def __init__(self, titularCont, iban):
        # aribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    # metode
    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print('------------------------------')


    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('PIN gresit')
            #self.incercari_activare = self.incercari_activare + 1
            self.incercari_activare += 1


    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat cu {suma}')
        print(f'Aveti in cont {self.sold}')


    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma  # scadem suma din sold
            print(f'Ati cheltuit suma {suma}')
            print(f'Mai aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')

    def salut(self):
        print(f'Buna {self.titularCont}')





cont1 = ContBancar('Geo A', 'RO001')
cont2 = ContBancar('Andrei A', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300)
cont2.plataCard(100)
cont2.plataCard(200)


cont1.interogareSold()
cont2.interogareSold()

