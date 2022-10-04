
#Listy

# Zadanie 1
print("************ Zadanie 1 ***************")
# 1a)
lista1 = [x for x in range(1,11)]
print(lista1)

# 1b)
lista2 =  [x for x in range(21) if x%2==0]
print(lista2)

# 1c)
lista3 = [x**2 for x in range(1,11)]
print(lista3)

# 1d)
lista4 = [0 for x in range(10)]
print(lista4)

# 1e)
lista5 = [x%2 for x in range(10)]
print(lista5)

# 1f)
lista6 = [x%5 for x in range(10)]
print(lista6)

# Zadanie 2
print("************ Zadanie 2 ***************")
# 2a)
lista2a = []
i = 1
while len(lista2a) < 10:
    lista2a.append(i)
    i = i + 1
print(lista2a)

# 2b)
lista2b = []
i = 0
while len(lista2b) < 11:
    lista2b.append(i*2)
    i = i + 1
print(lista2b)

# 2c)
lista2c = []
i = 1
while len(lista2c) < 10:
    lista2c.append(i**2)
    i = i + 1
print(lista2c)

# 2d)
lista2d = []
i = 0
while len(lista2d) < 10:
    lista2d.append(0)
    i = i + 1
print(lista2d)

# 2e)
lista2e = []
i = 0
while len(lista2e) < 10:
    lista2e.append(i%2)
    i = i + 1
print(lista2e)

# 2f)
lista2f = []
i = 0
while len(lista2f) < 10:
    lista2f.append(i%5)
    i = i + 1
print(lista2f)

# Zadanie 3
print("************ Zadanie 3 ***************")

def ile_ujemnych(lista33):
    suma=0
    for x in lista33:
        if x < 0:
            suma = suma + 1
    return suma

lista3 = [1,2,-3,-5,-2,10,11,-1]
print(ile_ujemnych(lista3))

# Zadanie 4
print("************ Zadanie 4 ***************")

def iloczyn(lista44):
    iloczyn=1
    for x in lista44:
        iloczyn=x*iloczyn
    return iloczyn

lista4 = [1,3,2,5,10]
print(iloczyn(lista4))

# Zadanie 5
print("************ Zadanie 5 ***************")

def minmax(lista55):
    min=10000
    max=-9999
    for x in lista55:
        if x < min:
            min=x
        if x > max:
            max=x
    return (min,max)

lista5 = [-32,1,-4,2,5,10,-9]
print(minmax(lista5))

# Zadanie 6
print("************ Zadanie 6 ***************")

def suma_przemienna(lista66):
    suma2=0
    znaki=1
    for x in lista66:
        suma2 += znaki*x
        znaki = -1 * znaki

    return (suma2)

lista6 = [1,4,16,9,9,7,4,9,11]
print(suma_przemienna(lista6))

# Zadanie 7
print("************ Zadanie 7 ***************")

def dodaj(lista77,cyfra):
    if len(lista77)==10:
        return lista77
    lista77.append(cyfra)
    return lista77

lista7 = [1,2,3,4,5,6,7,8,9,]
print(dodaj(lista7,-5))

# Zadanie 8
print("************ Zadanie 8 ***************")
lista8 = [x for x in range(2,10000)]
for x in lista8:
    if x%2==0 :
        lista8.remove(x)
    elif x%3==0:
        lista8.remove(x)
print(lista8)










