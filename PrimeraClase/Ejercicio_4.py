class Vehiculo:
    marca: str
    combustible: str
    tipo: str
    combustible_maximo: float
    combustible_restante: float
    
    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
    
    def encender(self):
        if(self.combustible_restante*100)/self.combustible_maximo < 10:
            print("El Nivel de combustible esta muy bajo, vaya a repostar")
        else:
            print("Tiene un nivel optimo de combustible")
    
    def arrancar(self):
        pass
    
    def __str__(self): 
        return "El vehiculo de tipo {}, y marca {} necesita gasolina {} para operar".format(self.tipo,self.marca, self.combustible)
    
class Carro(Vehiculo):
    def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Carro'
      self.combustible_maximo = 3
      self.combustible_restante = 1

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Moto'
      self.combustible_maximo = 25
      self.combustible_restante = 1.2


carro = Carro('Chevrolet', 'diesel')
carro.encender()
print(carro)
print("--"*30)
moto = Moto('Royal Enfield', 'corriente')
moto.encender()
print(moto)