# "Zadanie 3"
# Stwórz iterator i generator, które będą zwracały n liczb niepodzielnych
# przez m.
# np. dla n=10, m=3: [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]

# Tradycyjnie

def tradycyjnie(n, m):
    lista = []
    for i in range(n*m):
        if i % m != 0:
            lista.append(i)
        elif len(lista) == n:
            break

    return lista

print(tradycyjnie(10, 3))

# Generatorem

def generator(n, m):
    lista = []
    for i in range(n*m):
        if i % m != 0:
            lista.append(i)
        elif len(lista) == n:
            break

    yield lista           # yield jest zamiast return

for i in generator(10, 3):
    print(i)
    
    
# Tu masz przykładowe zadanie z iteratorem żeby obczaić konstrukcję

# Zadanie
# Napisz iterator i generator zwracające kwadrat danej liczby
#  gdy n = 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Generator

def kwadrat_generator(n):
    suma = 0
    for i in range(1, n + 1):
        suma = i*i
        yield suma

for i in kwadrat_generator(10):
    print(i)
    
# Albo druga wersja z while

def sum_generator2(n):
    suma = 0
    i = 1
    while i != n + 1:
        suma += i
        i += 1
        yield suma
for i in sum_generator2(10):
    print(i)

# A tak wygląda Iterator

class PowerIterator:
    def __init__(self, n):
        self.n = n
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= self.n:
            raise StopIteration     # tu masz warunek żeby zatrzymać iteracje
        self.number += 1
        return self.number ** 2

for i in PowerIterator(10):
    print(i)
