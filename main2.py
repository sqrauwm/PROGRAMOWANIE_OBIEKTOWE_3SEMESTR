
# Zadanie 2.1

# def mult(abc):
#     wynik = 1
#     for x in range(0,len(abc)):
#         wynik = wynik * abc[x]
#     return wynik
#
# print(mult([3, 5, 7]))
# print(mult(range(2,8,2)))

# Zadanie 2.2

# def multi_ints(a2):
#     wynik = 1
#     for x in range(0, len(a2)):
#         if(type(a2[x]) == int):
#             wynik = wynik * a2[x]
#     return wynik
#
# print(multi_ints([3, 3.14, 5, "abc", 7]))

# Zadanie 2.3

# def multiply(*args):
#     wynik = 1
#     for x in args:
#         wynik = wynik * x
#     return wynik
#
# print(multiply(3,5,7))

# Zadanie 2.4

# def multiply_ints(*args):
#     wynik = 1
#     for x in args:
#         if(type(x) == int):
#             wynik = wynik * x
#     return wynik
#
# print(multiply_ints(3, 3.14, 5, "abc", 7))

# Zadanie 2.5

# def make_car(firma, model, **kwargs):
#     slownik = kwargs
#     slownik['Firma:'] = firma
#     slownik['Model:'] = model
#
#     return (slownik)
#
# print(make_car("Kia", "Picanto", kolor="roz"))

# Zadanie 3.1

# lista = []
# lista.append([x for x in range(1, 11)])
# lista.append([x ** 2 for x in range(1, 11)])
# lista.append([x ** 3 for x in range(1, 11)])
# for i in lista:
#     print(f"[{i}]")

# Zadanie 3.2
lista2=[]
suma=0
suma2=0
for x in range(1,11):
    lista2.append([x for x in range(1, x+1)])
    suma = suma + x
    suma2=suma2+suma
    print(suma)

for y in lista2:
    print(f"{y}")
print(suma2)














