
class Adres(object):
    def __init__(self, ulica, nr_dom, miasto,kod_poc, nr_mie=None):
        self.ulica = ulica
        self.nr_dom = nr_dom
        self.miasto = miasto
        self.kod_poc = kod_poc

        if nr_mie is not None:
            self.nr_mie = nr_mie

    def show(self) -> None:
        if hasattr(self, 'nr_mie'):
            print(f'{self.ulica} {self.nr_dom}/{self.nr_mie}')
            print(f'{self.kod_poc} {self.miasto}')
            return None
        print(f'{self.ulica} {self.nr_dom}')
        print(f'{self.kod_poc} {self.miasto}')

    def comes_before(self, other):
        for i in range(0,len(self.kod_poc)):
            if self.kod_poc[i] == other.kod_poc[i]:
                continue
            if self.kod_poc[i] < other.kod_poc[i]:
                return True
            return False

adres1 = Adres('Lotnicza',22,'Warszawa','22-311')
adres2 = Adres('Warszawska',35,'Olsztyn','22-122',5)
adres1.show()
adres2.show()
print(adres1.comes_before(adres2))


