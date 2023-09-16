class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.mensaje_id = 1 

    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor):
        valor['id'] = self.mensaje_id
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
        self.mensaje_id += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        nodo_actual = self.primero
        nuevo_id = 1
        while nodo_actual:
            nodo_actual.valor['id'] = nuevo_id
            nuevo_id += 1
            nodo_actual = nodo_actual.siguiente

        return valor


    def desencolar_id(self, mensaje_id):
        nodo_actual = self.primero
        nodo_anterior = None
        while nodo_actual:
            if nodo_actual.valor['id'] == mensaje_id:
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                else:
                    self.primero = nodo_actual.siguiente
                if nodo_actual == self.ultimo:
                    self.ultimo = nodo_anterior

                nodo_renumerar = self.primero
                nuevo_id = 1
                while nodo_renumerar:
                    nodo_renumerar.valor['id'] = nuevo_id
                    nuevo_id += 1
                    nodo_renumerar = nodo_renumerar.siguiente

                return nodo_actual.valor
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None


    def ver_listado(self):
        elementos = []
        nodo_actual = self.primero
        while nodo_actual:
            elementos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return elementos

    def ver_primero(self):
        if not self.esta_vacia():
            return self.primero.valor
        else:
            return None

    def ver_ultimo(self):
        if not self.esta_vacia():
            return self.ultimo.valor
        else:
            return None

    def contar(self):
        contador = 0
        nodo_actual = self.primero
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador
