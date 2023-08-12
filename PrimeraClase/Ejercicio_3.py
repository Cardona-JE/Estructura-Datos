class Vehiculo:
    marca: str
    combustible: str
    tipo: str

    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
    
    def encender(self):
        pass
    def arrancar(self):
        pass

    def __str__(self): 
        return "El vehiculo de tipo {}, y marca {} necesita gasolina {} para operar".format(self.tipo,self.marca, self.combustible)

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Carro'

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Moto'


carro = Carro('Chevrolet', 'diesel')
moto = Moto('Royal Enfield', 'corriente')
print(carro)
print(moto)