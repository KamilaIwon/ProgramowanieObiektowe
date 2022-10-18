
class Car:
    def __init__(self, wydajnosc: float, max_paliwo: float):
        self.wydajnosc = wydajnosc
        self.max_paliwo = max_paliwo
        self.poczatkowe_paliwo = 0

    def drive(self, dystans: float) -> None:
        ile = dystans / self.wydajnosc
        if ile > self.poczatkowe_paliwo:
            print('Nie ma tyle paliwa w baku:')
            return None
        self.poczatkowe_paliwo -= dystans / self.wydajnosc

    def get_fuel_level(self) -> float:
        return self.poczatkowe_paliwo

    def add_fuel(self, ilosc: float) -> None:
        if ilosc + self.poczatkowe_paliwo > self.max_paliwo:
            print('Nie ma tyle miejsca:')
            return None
        self.poczatkowe_paliwo += ilosc

my_car = Car(20, 40) # Wydajnosc 20 km/litr, pojemnosc baku 40
my_car.add_fuel(30) # Zatankuj co najwyzej 30 litrów
my_car.drive(100) # Przejedz 100 m
print(my_car.get_fuel_level()) # Wydrukuj ilosc pozostałego paliwa
