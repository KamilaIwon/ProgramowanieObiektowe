from Court1 import Court
from Stadium1 import Stadium
court_1 = Court(address='Słoneczna 10, 10-100 Olsztyn', year_built=1999)
print(court_1)
court_2 = Court(500, 500, 'Słoneczna 10, 10-100 Olsztyn', 1999)
print(court_2)
court_3 = Court(100, 50, 'Słoneczna 10, 10-100 Olsztyn', 1999)
court_3.width = 50
court_3.length = 100
print(court_3)
print(court_1.length)
court_1.year_built = 1990
print(court_1)
print(court_1.area())
court_1.year_built = 2030
print(court_1)
Court.validate(court_1)
print(court_1)
print("--------------------------------")
stadium_1 = Stadium(address='Słoneczna 10, 10-100 Olsztyn', year_built=1999,
                    name='Słoneczny stadion', common_name='Słoneczko', capacity=10000)
print(stadium_1)
stadium_2 = Stadium(address='Słoneczna 10, 10-100 Olsztyn', year_built=1999,
                    name='Słoneczny stadion', capacity=10000)
print(stadium_2)
