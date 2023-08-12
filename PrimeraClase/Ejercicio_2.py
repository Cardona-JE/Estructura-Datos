class Vehiculo:
    marca: str
    combustible: str

    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
    
    def encender(self):
        pass
    def arrancar(self):
        pass

    def __str__(self): 
        return "El vehiculo {} necesita gasolina {} para operar".format(self.marca, self.combustible)

class Carro(Vehiculo):
    pass

class Moto(Vehiculo):
    pass


carro = Carro('Chevrolet', 'diesel')
moto = Moto('Royal Enfield', 'corriente')
print(carro)
print(moto)