class Pokoj:
    def __init__(self, swiat, nazwa, inne_lokalizacje, opis):
        self.swiat = swiat
        self.nazwa = nazwa
        self.inne_lokalizacje = inne_lokalizacje
        self.opis = opis

    def opisz_sie(self):
        print(self.opis)
        if self.nazwa == 'podwórko' and not self.swiat.podniesiona_szczotka:
            print("Widzisz szczotke. Wyglada jak do muszli.")

    def sasiednie_pokoje(self):
        return list(map(swiat.pokoj_po_nazwie, self.inne_lokalizacje))


class Swiat:
    def __init__(self):
        self.mapa = [
            Pokoj(self, 'salon', ['kuchnia', 'sypialnia', 'łazienka', 'przedsionek'], 'Ładnie tutaj'),
            Pokoj(self, 'sypialnia', ['salon'], 'Widzisz miękkie łóżko'),
            Pokoj(self, 'łazienka', ['salon'], 'Trochę brudna ta muszka'),
            Pokoj(self, 'kuchnia', ['salon'], 'Zwykła kuchnia'),
            Pokoj(self, 'przedsionek', ['salon', 'podwórko'], 'Ładnie tu'),
            Pokoj(self, 'podwórko', ['przedsionek'], 'Trawa')
        ]

        self.podniesiona_szczotka = False

        self.aktualne_miejsce = self.pokoj_po_nazwie('łazienka')

    def przedstaw_pokoj(self):
        pokoj = self.aktualne_miejsce

        print('-' * 40)
        print(f'Jesteś aktualnie w {pokoj.nazwa}')
        print()
        pokoj.opisz_sie()
        print()
        print('Możesz iść do:')
        if pokoj.nazwa == 'podwórko' and not self.podniesiona_szczotka:
            print('0. podnieść szczotke')
        if pokoj.nazwa == 'łazienka' and self.podniesiona_szczotka:
            print('0. Umyj muszle')

        for i, sasiad in enumerate(pokoj.sasiednie_pokoje()):
            print(f'{i + 1}. {sasiad.nazwa}')

    def pokoj_po_nazwie(self, nazwa):
        for pokoj in self.mapa:
            if pokoj.nazwa == nazwa:
                return pokoj
        raise Exception(f'Nieznany pokoj {nazwa}')

    def wykonaj_ruch(self):
        try:
            rzadnie_cyferka = int(input('Gdzie chcesz isc? ').strip())
        except ValueError:
            print("Podaj cyferkę")
            return self.wykonaj_ruch()

        if rzadnie_cyferka == 0 and self.aktualne_miejsce.nazwa == 'podwórko' and not self.podniesiona_szczotka:
            print('')
            print("Sczotka podniesiona!")
            self.podniesiona_szczotka = True

        elif rzadnie_cyferka == 0 and self.aktualne_miejsce.nazwa == 'łazienka' and self.podniesiona_szczotka:
            print("Brawo!. Muszla umyta!")
            exit()

        elif rzadnie_cyferka <= 0 or len(self.aktualne_miejsce.sasiednie_pokoje()) < rzadnie_cyferka:
            print("Nie wiem co to za pokój")
            self.wykonaj_ruch()
        else:
            nowy = self.aktualne_miejsce.sasiednie_pokoje()[rzadnie_cyferka - 1]
            swiat.aktualne_miejsce = nowy


swiat = Swiat()
print('Włąsnie skończyłeś bardzo ważną sprawę,\nale nie widzisz nigdzie szczotki do wyczuszczenia muszki.\nZnajdź ją!')

while True:
    swiat.przedstaw_pokoj()
    swiat.wykonaj_ruch()