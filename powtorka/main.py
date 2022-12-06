from court import Court
from stadium import Stadium

court_1 = Court(address='Słoneczna 10', year_built=1999)
# print(court_1)

# court_2 = Court(500, 500, 'Słoneczna 10', 1999)
# print(court_2)

# court_3 = Court(50, 100, 'Słoneczna 10', 1999)
# print(court_3)

# print(court_1.length)
# court_1.year_built = 1990
# print(court_1)
# print(court_1.area())
# court_1.year_built = 2030
# print(court_1)
# Court.validate(court_1)
# print(court_1)

#
stadium_1 = Stadium(address='Słoneczna 10', year_built=1999, name='Słoneczny stadion',
                    common_name='słoneczko', capacity=10000)

print(stadium_1)

stadium_2 = Stadium(50, 100, 'Słoneczna 10', 1999, 'Słoneczny stadion', capacity=10000)
# print(stadium_2)
stadium_1.year_built = 2030
print(stadium_1)

Stadium.validate(stadium_1)
print(stadium_1)

print(stadium_1 == stadium_2)
stadium_1.width = 50.0
stadium_1.length = 100.0
print(stadium_1)
print(stadium_2)
print(stadium_1 == stadium_2)
print(stadium_1 != stadium_2)
stadium_1.capacity = 500
print(stadium_1 == stadium_2)
