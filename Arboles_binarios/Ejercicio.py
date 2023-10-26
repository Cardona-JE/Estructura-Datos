import random
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.left = None
        self.right = None
class Arbol:
    def __init__(self,dato):
        self.raiz = Nodo(dato)
    
    def agregar_dato(self,nodo,dato):
        if dato < nodo.dato : 
            if nodo.left is None:
                nodo.left = Nodo(dato)
            else:
                self.agregar_dato(nodo.left,dato)
        else:
            if nodo.right is None:
                nodo.right = Nodo(dato)
            else:
                self.agregar_dato(nodo.right,dato)
    def impresion_inorden(self,nodo):
        if nodo is not None:
            self.impresion_inorden(nodo.left)
            print(nodo.dato, end=", ")
            self.impresion_inorden(nodo.right)
    def agregar(self, dato):
        self.agregar_dato(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.impresion_inorden(self.raiz)
        print("")
xd = random.randint(1,50)
print(xd)
arbol = Arbol(xd)
numero = 1
while numero < 5:
    hola = random.randint(1,50) 
    print(hola)
    arbol.agregar(hola)
    numero += 1

