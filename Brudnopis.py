from math import sqrt
from datetime import datetime

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prime_generator(n):
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            yield number
            generated_numbers += 1
        number += 1


lst = prime_generator(5000)
for i in lst:
    print(i)
    print(lst)

    
#     ROZWIĄZANIE

# Zadanie 3
# Stwórz iterator i generator, które będą zwracały n liczb niepodzielnych
# przez m.
# np. dla n=10, m=3: [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]

class IndivisableIterator:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.i = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.counter == self.n:
            raise StopIteration
        if self.i % self.m != 0:
            self.counter += 1
            return self.i
        return self.__next__()

for i in IndivisableIterator(10,3):
    print(i, end=", ")

# Generator

def indevisible_generator(n, m):
    number = 0
    count = 0
    while count < n:
        if number %  m != 0:
            yield number
            count +=1
        number += 1

for i in indevisible_generator(10,3):
    print(i, end=", ")
