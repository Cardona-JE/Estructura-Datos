import json

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.anterior = None
        self.siguiente = None
        self.id = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.ultimo_id = 0

    def agregar(self, datos):
        nuevo_nodo = Nodo(datos)
        self.ultimo_id += 1
        nuevo_nodo.id = self.ultimo_id
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

# Cargar datos desde el archivo JSON
datos_json = json.load(open('resultados_celulares.json'))

# Crear lista doblemente enlazada
lista_datos = ListaDoblementeEnlazada()

for datos_celular in datos_json:
    lista_datos.agregar(datos_celular)

# Mostrar datos de la lista
actual = lista_datos.cabeza
while actual:
    print(f"ID: {actual.id}")
    for clave, valor in actual.datos.items():
        print(f"{clave}: {valor}")
    print()
    actual = actual.siguiente
