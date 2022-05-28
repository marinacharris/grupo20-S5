lista = []
bases = [5,1,4,8,7,3]
for i in range(9):
    lista.append(i)
print(lista)

# sintaxis: expresion for i in onjeto iterable
lista = [i for i in range(9)]
print(lista)
lista = [i for i in 'Marina']
print(lista)
lista = [i**2 for i in bases]
print(lista)
lista = list(map(lambda x: x**2,bases))
print(lista)

#crear una lista con los numeros pares del 0 al 50
#programación imperativa
lista = []
for i in range(51):
    if i%2 == 0:
        lista.append(i)
print(lista)

# sintaxis con if
# sintaxis: expresion for i in onjeto iterable if condicion

lista = [i for i in range(51) if i%2 == 0]
print(lista)

lista = list(filter(lambda x: x%2==1,range(51)))
print(lista)

