import math
##x = [1, 9, 0, 20, -4, 12, 16, 7]
##suma = 0
##print(suma)


def printPairs(arr, n, sum):
    # count = 0

    # Suma de todos los posibles valores de parejas y las sumas
    # pairs and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep="")


# Codigo
y =int(input("ingrese el numero de la suma que desea identificar: "))
arr = []
size_arr = int(input("Ingrese un valos entero para definir el tamaño de la lista: "))
for size_arr in range(size_arr):
    valor = int(input("Ingrese valor entero en la lista: "))
    arr.append(valor)

print(arr)
n = len(arr)
sum = y
printPairs(arr, n, sum)
