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
        if (self.combustible_restante * 100) / self.combustible_maximo < 10:
            print("El Nivel de combustible está muy bajo, vaya a repostar")
            self.arrancar()
        else:
            print("Tiene un nivel óptimo de combustible")
            self.arrancar()
    
    def arrancar(self):
        if self.combustible_restante <= 0:
            print("¡Sin combustible! El vehículo no puede arrancar.")
        else:
            print("Arrancando el vehículo...")
            while self.combustible_restante > 0:
                self.realizar_marcha()
    
    def realizar_marcha(self):
        if self.combustible_restante > 0:
            print("Vehículo en marcha. Nivel de combustible:", self.combustible_restante)
            self.combustible_restante -= 0.5  # Con esto se simula que el vehiculo disminuya su gasolina 
        if (self.combustible_restante * 100) / self.combustible_maximo <= 10:
            print("Advertencia: Nivel de combustible bajo.")
        if self.combustible_restante <= 0:
            self.detener()       
    
    def detener(self):
        if self.combustible_restante <= 0:
            print("--" * 30)
            print("¡Sin combustible! El vehículo se detendrá.")
            print("Vehículo apagado.")
            print("--" * 30)
            self.repostar()
    
    def repostar(self):
        desicion = int(input("Si desea repostar diga Si o No (Si = 1, No = 0): "))
        if desicion == 1:
            print("El numero maximo de galones es: ",self.combustible_maximo)
            while True:
                cantidad_repuesto = int(input("Ingrese el valor en galones a repostar:"))
                if cantidad_repuesto <= self.combustible_maximo:
                    self.combustible_restante = cantidad_repuesto
                    self.encender()
                    break  
                else: 
                    print("El valor ingresado es mayor al máximo permitido. Intente nuevamente.")
    
    def __str__(self): 
        return "El vehículo de tipo {}, y marca {} necesita gasolina {} para operar".format(self.tipo, self.marca, self.combustible)


class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = 'Carro'
        self.combustible_maximo = 30
        self.combustible_restante = 10

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = 'Moto'
        self.combustible_maximo = 25
        self.combustible_restante = 10


carro = Carro('Chevrolet', 'diesel')
print(carro)
carro.encender()

print("--" * 30)

moto = Moto('Royal Enfield', 'corriente')
print(moto)
moto.encender()
