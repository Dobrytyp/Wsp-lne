def dupa(n):
    lista = []
    if n == 0:
        return lista
    elif n % 3 == 0:
        lista.append(n)
        dupa(n - 1)
    else:
        dupa(n - 1)
    
print(dupa(10))
