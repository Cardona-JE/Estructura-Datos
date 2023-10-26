"""Se importa el modulo random para generar numeros aleatorios"""
import random
"""Se importa el modulo time para medir el tiempo de ejecucion"""
import time


def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr
  
def buscar(datico,arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == datico:
            return("pa su numero si esta")
            break


inicio = time.time()
random.seed(10)
datos = [random.randint(0, 10000) for _ in range(5000)]
ordenado = bubble_sort(datos)
print(ordenado)
fin = time.time()
print("Tiempo de ejecucion: ", fin-inicio)

datico = int(input("Indique el numero que desea buscar: "))
inicio_b = time.time()
dato_b = buscar(datico,datos)
print(dato_b)
fin_b = time.time()
print("lista: La busqueda se demoro: ", fin_b-inicio_b)

inicio_c = time.time()
print("Su valor minimo en la lista es: ", min(ordenado))
fin_c = time.time()
print("lista: La busqueda del valor minimo fue de: ", fin_c-inicio_c)

#Tambien se puede hacer de esta forma (Despues de ordenar todos los datos)

inicio_c = time.time()
print("Su valor minimo en la lista es: ", ordenado[0])
fin_c = time.time()
print("lista: La busqueda del valor minimo fue de: ", fin_c-inicio_c)